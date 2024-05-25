'''
Python provides a no of different, different modules for different, different purposes. 
Using python, we can get notifications on our system.
Python provides a 'plyer' module to work with notifications.
This plyer module provides different functions that can take different parameters like title, message, icon to display the notification
NOTE: We can run this in the background as well. To get notified for every 1 hr or any other specified time delay.
        To do this we need to run the program using -
        
            *** "pythonw filename.py" ***

        To stop this background process running 
            1.go to task manager
            2.processes
            3.python process>stop
'''

from plyer import notification
#to add some time delay between the notifications.
import time

def notify(title, message):
    """
    Display a notification with the specified title and message.

    Args:
        title (str): The title of the notification.
        message (str): The message content of the notification.
    """
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # If you want to use a custom icon, provide the path here
        timeout=10  # The notification will automatically disappear after 10 seconds
    )

# Example usage:
if __name__ == "__main__":
    title = "*** Take Rest ***"
    message = "Any Description About the title. Remember it should not be too longgg!!!"
    notify(title, message)
