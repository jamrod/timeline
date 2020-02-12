# Timeline
###### A micro journaling application

## Project Description
Timeline is an app that takes *time capsules* to record your thoughts, memories, and whatever are connected to them. Initially, it will log text notes, but will eventually take images, urls, songs, and much more. These will all be displayed and organized by timestamp. This will provide the user with the ability to view those special moments in a chronological order. 

Timeline has full CRUD functionality for creating *timelines* and *time capsules* that populate them. These can be created, read, updated, and deleted by the users. Once created, they display in chronological order based upon their creation date. 


### Technologies
Built with Python, using the Django framework with Postgresql for the database.

#### Dependencies
[Python 3](https://docs.python.org/3/)
[Django](https://docs.djangoproject.com/en/3.0/)
[Postgresql](https://www.postgresql.org/docs/)
[psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

### MVP/PostMVP

#### MVP
##### Bronze
- Front-End CRUD
- Back-End CRUD

#### Post MVP
##### Silver
- Users & Authentication
    - user-owner only access for edits
- Date/Time Stamp
- Tags 

##### Gold
- Shared Timelines
    - Read-only access
- Random Time Capsule (think 'timehop')
    - presented at login
- Time Capsule upgrades
    - Images
    - Sound Files
        - with player ability
    - Clickable links to sites, videos, etc
- Status
    - public/private

## Models
- Timeline
    - Author
- Time_Capsule
    - Timeline: Foreign Key
    - Timestamp: DateField
    - Contents: TextField

## Code Snippet
Here is a snippet of code that feeds into the Timeline model to generate the *time capsule*. 
```
class Time_Capsule(models.Model):
    timeline = models.ForeignKey(
        Timeline, on_delete=models.CASCADE, related_name='time_capsules')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    contents = models.TextField(default='')

    def __str__(self):
        return self.contents + str(self.created_on)
```



## Issues and Resolutions
We ran into an issue with the timestamp that prevent the content from rendering at certain levels, The error presented was an issue with the timestamp not being a string. 

**ERROR**
```
    def __str__(self):
        return self.contents
```
**RESOLUTION**
```
    def __str__(self):
        return self.contents + str(self.created_on)
```