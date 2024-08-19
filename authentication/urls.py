from django.urls import path


from .views import login_page,signin_page,home,logout,contact,register,recruit,myevents,organizerevents,event_register,manage_events,approve_event,delete_event,detailed_event,unregister,org_manage_event,showParticipants,showVolunteers
urlpatterns = [
    path('',home,name='home'),
    path('login/',login_page,name='login'),
    path('signup/',signin_page,name='signup'),
    path('logout/',logout,name='logout'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('unregister/',unregister,name='unregister'),
    path('recruit/<int:event_id>',recruit,name='recrute'),
    path('myevents/',myevents,name='myevents'),
    path('event_register/',event_register,name='event_register'),
    path('manage_events/',manage_events,name='manage_events'),
    path('organizer_events/',organizerevents,name='organizerevents'),
    path('detailed_event/<int:event_id>/',detailed_event,name='detailed_event'),
    path('approve_event/<int:event_id>/',approve_event, name='approve_event'),
    path('org_manage_event/<int:event_id>',org_manage_event,name='org_manage_event'),
    path('showParticipants/<int:event_id>',showParticipants,name='showParticipants'),
    path('showVolunteers/<int:event_id>',showVolunteers,name='showVolunteers'),
    path('delete_event/<int:event_id>/',delete_event, name='delete_event'),
]



