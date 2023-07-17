from winotify import Notification
toast=Notification(app_id="Aratrika Purkait",
                   title="Message Title",
                   msg="Hello! This is Aratrika",
                   duration="short",
                   icon=r"C:\Users\hp\Downloads\WhatsApp Image 2023-02-08 at 20.34.22.jpg")
toast.show()