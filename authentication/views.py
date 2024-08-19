# Import necessary modules and models
import datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from .models import *

# Define a view function for the home page
def home(request):
	events = Event.objects.filter(approved=True).order_by('-start_time')[:5]
	pastevents = Event.objects.filter(end_time__lt=datetime.date.today()).order_by('-start_time')[:5]
	user = request.user

	if not user.is_authenticated:
		return render(request, 'authentication/index.html', {'images': Photos.objects.all(), 'events': events, 'past_events': pastevents})

	registrations = Registration.objects.filter(user=Profile.objects.get(user=user))
	registeredEvents = [registration.event for registration in registrations]
	role = Profile.objects.get(user=user).role
	return render(request, 'authentication/index.html', {'images': Photos.objects.all(), 'events': events, 'past_events': pastevents, 'role': role, 'registeredEvents': registeredEvents})

# Define a view function for the login page
def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			print("Invalid Username")
			messages.error(request, 'Invalid Username')

			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			try:
				html_message = render_to_string('authentication/loginAlert.html', {'user': user})
				recipiants=[user.email,]
				send_html_email('Login Alert', html_message, from_email=settings.EMAIL_HOST_USER, recipiant=recipiants)
				#send_mail( 'Login Alert', 'some one is is loged in into your event management user account', from_email=settings.EMAIL_HOST_USER, recipient_list=recipiants )
				return redirect('/')
			except:
				return redirect('/')
	# Render the login page template (GET request)
	return render(request, 'authentication/login.html')

# Define a view function for the registration page
def signin_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		username = request.POST.get('username')
		email=request.POST.get('email')
		password = request.POST.get('password')
		gender=request.POST.get('gender')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/signup/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username,
			email=email
		)
		
		# Create a new Profile object for the user
		profile = Profile(user=user, gender=gender)
		profile.save()
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()

		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		try:
				html_message = render_to_string('authentication/signupAlert.html', {'user': user})
				recipiants=[user.email,]
				send_html_email('Account Created Successfully', html_message, from_email=settings.EMAIL_HOST_USER, recipiant=recipiants)
				#send_mail( 'Login Alert', 'some one is is loged in into your event management user account', from_email=settings.EMAIL_HOST_USER, recipient_list=recipiants )
				return redirect('/login/')
		except:
				return redirect('/login/')
	# Render the registration page template (GET request)
	return render(request, 'authentication/signup.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def contact(request):
	if request.method=="GET":
		name=request.GET.get('name')
		mail=request.GET.get('mail')
		number=request.GET.get('number')
		subject=request.GET.get('subject')
		message=request.GET.get('message')
		temp=Contact(name=name,mail=mail,number=number,subject=subject,message=message)
		temp.save()
		messages.info(request, "Message Sent Successfully! We will get back to you soon")
		return redirect('/')
	
def register(request):
	if request.method=="POST":
		event_name=request.POST.get('event_name')
		print(event_name)
		user=request.user
		if(user.is_authenticated):
			try:
				r1=Registration(event=Event.objects.get(name=event_name),user=Profile.objects.get(user=user))
				r1.save()
				html_message = render_to_string('authentication/regsuccessAlertmail.html', {'user': user})
				recipiants=[user.email,]
				send_html_email('Registered Successfully', html_message, from_email=settings.EMAIL_HOST_USER, recipiant=recipiants)
				messages.info(request, "Registered Succesfully ,check in MY EVENTS for more info !!")
				return redirect('/')
			except:
				messages.error(request, "Not Registered Try Again!!")
				return redirect('/')
		else:
			return redirect('/login/')
		
def unregister(request):
	if request.method=="POST":
		event_name=request.POST.get('event_name')
		user=request.user
		try:
			r1=Registration.objects.filter(event=Event.objects.get(name=event_name),user=Profile.objects.get(user=user))
			r1.delete()
			messages.info(request, "Unregistered Succesfully ,check in MY EVENTS for more info !!")
			return redirect('/')
		except:
			messages.error(request, "Not Unregistered Try Again!!")
			return redirect('/')
		else:
			return redirect('/login/')

		

def recruit(request,event_id):
	user=request.user
	if request.method=="POST":
		task=request.POST.get('task')
		event_id=request.POST.get('event_id')
		event=Event.objects.get(id=event_id)
		user=Profile.objects.get(user=user)
		v1=Volunteer(event=event,user=user,role=task)
		v1.save()
		messages.info(request, "Applied for Volunteer Succesfully ,We will get back to you soon !!")
		return redirect('/')
	
	if(user.is_authenticated):
		return render(request,"authentication/register.html",{'event_id':event_id})
	return render(request,"authentication/login.html")


def myevents(request):
	try:
		user = request.user
		registrations = Registration.objects.filter(user=Profile.objects.get(user=user))
		events = [registration.event for registration in registrations]
		return render(request, 'authentication/myevents.html', {'events': events})
	except:
		return redirect('/login/')


def organizerevents(request):
	user = request.user
	events = Event.objects.filter(organizer=Profile.objects.get(user=user))
	return render(request,'authentication/org.html',{'events':events})


def event_register(request):
	user=request.user
	if user.is_authenticated:
		if request.method == "POST":
			user = request.user
			event_name = request.POST.get('event_name')
			start_time = request.POST.get('start_date')
			end_time = request.POST.get('end_date')
			venue = request.POST.get('venue')
			description = request.POST.get('description')
			r1=Event(name=event_name,description=description,start_time=start_time,end_time=end_time,venue=venue,organizer=Profile.objects.get(user=user))
			r1.save()
			return redirect('/')
	else:
		return redirect('/login/')
	
	return render(request, 'authentication/eventRegister.html')


def manage_events(request):
	events=Event.objects.filter(approved=False)
	return render(request,'authentication/admin.html',{'events':events})


def approve_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.approved = True
    profile=event.organizer
    profile.role='organizer'
    event.save()
    profile.save()

    return redirect('manage_events')  # Replace 'admin_page' with the name of your admin page URL

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('manage_events')  # Replace 'admin_page' with the name of your admin page URL

def org_manage_event(request,event_id):
	event=Event.objects.get(id=event_id)
	registrations=Registration.objects.filter(event=event)
	regCount=registrations.count()
	regMaleCount = registrations.filter(user__gender='male').count()
	regFemaleCount= registrations.filter(user__gender='female').count()
	volunteers=Volunteer.objects.filter(event=Event.objects.get(id=event_id))
	volunteersCount=volunteers.count()
	return render(request,'authentication/orgshow.html',{'regCount':regCount,'regMaleCount':regMaleCount,'regFemaleCount':regFemaleCount,'volunteersCount':volunteersCount,'event':event})

def showParticipants(request,event_id):
	registrations=Registration.objects.filter(event=Event.objects.get(id=event_id))
	return render(request,'authentication/participants.html',{'participants':registrations})

def showVolunteers(request,event_id):
	volunteers=Volunteer.objects.filter(event=Event.objects.get(id=event_id))
	return render(request,'authentication/volunteers.html',{'volunteers':volunteers})

def detailed_event(request,event_id):
	event = get_object_or_404(Event, id=event_id)
	return render(request,'authentication/showEvent.html',{'event':event})


def send_html_email(subject,html_content,from_email,recipiant):
	msg = EmailMessage(subject, html_content, from_email, recipiant)
	msg.content_subtype = "html"  # Main content is now text/html
	msg.send()