# Event Management System for RGUKT RK Valley
## TEAM KRYPTON

![Django](https://img.shields.io/badge/Django-5.0.7-green) ![HTML](https://img.shields.io/badge/HTML-5-orange) ![CSS](https://img.shields.io/badge/CSS-3-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES7-yellow)
### Index
- [overview](#Overview)
- [Features](#Key-Features)
- [Technologies Used](#Tech-Stack)
- [ Demo](#Demo)
- [Run Locally](#Installation-and-Setup)
- [Deployment](#Deployment)
- [collaborators](#Collaborators)
- [Thanks](#Thanks)


## Overview:
[**Krypton**](https://via.placeholder.com/10/00b48a?text=+) is a comprehensive web application  designed to streamline the planning, promotion, execution, and feedback process for campus events. This solution caters to students, faculty, and event organizers, providing a centralized platform for efficient event management in universitiy.
<img align="left" width=100% height=600px src="https://github.com/user-attachments/assets/ee3ed622-6522-4f35-a787-97399165f1cd">
## Key Features

- **User Authentication**: Secure login with *role-based access*(students, faculty, organizers,admin).
- **AI ChatBot:** Included chatbot with trained data regarding the *annual events,venues available etc.,university hierarchy and persmissions rules*.
- **Admin Dashboard :** To overview event details and give permissions access to conduct events.A supervisory authority with reference to *university hierarchy*.
- **Organizer's Dashboard:** Organiser can be student or faculty to effectively manage  events resources,registarations,volunteers.
- **User Dashboard**: Personalized dashboards displaying relevant information, registered events and tasks.
- **Events main page:** Details of the events based on their type as sports,education, entertainment highlighting upcoming,latest,past events with details.
- **Event Planning and Scheduling**: Tools for creating event timelines, task assignments, and venue booking.
- **Event Promotion and Registration**: Integrated promotion via social media, email, and in-app notifications; online registration and updates about event.
- **Volunteer Management**: Volunteer registaration forms, role assignments, and shift scheduling.
- **Resource Management**: Real-time tracking of event resources and equipment.
- **Real-Time Updates and Notifications**: 
Mail remainder system to the users about events,registrations,security alerts.(**SMTP**server used)
- **Feedback and Reviews :** Post-event surveys and event galleries.
## Installation and Setup
 1. ### Clone the repository:
``` bash 
git clone  https://github.com/Rajeswari-Machina/Krypton-Event-Management-System/
cd event-management-system
```
 2. ### Install dependencies:
```python
pip install -r requirements.txt
```
 3. ### Run migrations:
```python 
python manage.py migrate
```
 4. ### Start the development server:
```bash
python manage.py runserver
```
 5. ### Access the application:
``` Open your web browser and navigate to http://localhost:8000```

## Tech Stack

**Client:** HTML , CSS , JAVASCRIPT

**Server:** DJANGO 

**Databases:** SQLITE

## Demo
view at [click](https://www.linkedin.com/posts/rajeswari-machina_hackathon-webdevelopment-eventmanagement-activity-7226303647234547713-mejN?utm_source=share&utm_medium=member_desktop)


## Deployment

We used [pythonanywhere](https://www.pythonanywhere.com/) to host our website .
The website is live at [visit](https://teamkrypton.pythonanywhere.com/)
## Collaborators

| GitHub Profile                 |        Contribution    |
|--------------------------------------------|-----------------|
|[@Rajeswari Machina ](https://github.com/Rajeswari-Machina)           | Backend,Deployment,Documentation,email templates |
|[@Nishka Prasan](https://github.com/NishkaPrasan)     | Front End     |
| [@Vardhireddy Mani Kunar Reddy](https://github.com/Mani1655B)             | Backend ,Database |
| [@Gangavarapu Rameswar](https://github.com/RamEswar78)     | AI chatbot integration,backend |


Thank you to all the amazing contributors and collaborators who help make this project better! 🙌
##  Thanks 
[DEPT. OF CSE Student Recreation center Team](https://github.com/Student-Recreation-Center-CSE-RKV/SRC-s-Hackathon/tree/main?tab=readme-ov-file#problem-statement) for conducting Hackathon and providing us platform for developing solution to this problem.

[Viewers]() for paying your time for our solution.

## Support

For support, email rajeswarimachina02@gmail.com or contact our [Team](#Collaborators)
