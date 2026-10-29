CAMPUSCONNECT — CARTOON + MODERN LOST & FOUND
==============================================

या ZIP मध्ये तुमच्या Django project च्या source files आहेत. रंगीत cartoon-inspired design, animations, search/filter, login/signup आणि Lost/Found report form जोडले आहेत. तुमचा जुना database आणि virtual environment मुद्दाम ZIP मध्ये ठेवलेला नाही. त्यामुळे तुमची जुनी ZIP/फोल्डर backup म्हणून ठेवा.

सुरक्षितपणे वापरण्याची पद्धत:
1. ही ZIP extract करा. आत `campusconnect` folder मिळेल.
2. आधीच्या project folder ची backup copy ठेवा.
3. Extract केलेल्या `campusconnect` folder मधील source files वापरा. `db.sqlite3` जुना database असल्यास तुमच्या जुन्या project मधून नवीन folder मध्ये copy करा, म्हणजे आधीचे users/reports टिकतील.
4. VS Code मध्ये `campusconnect` folder उघडा. Terminal > New Terminal निवडा.
5. Windows PowerShell मध्ये virtual environment तयार/activate करा (जुना venv copy केलेला नाही):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
6. जर जुना `db.sqlite3` copy केला नसेल, तर:
   python manage.py migrate
   python manage.py createsuperuser
   (जुना database copy केला असल्यास आधी `python manage.py migrate` चालवा; superuser आधीच असेल तर पुन्हा तयार करू नका.)
7. `python manage.py check`
8. `python manage.py runserver`
9. Browser: http://127.0.0.1:8000/  | Admin: http://127.0.0.1:8000/admin/

टीप:
- Item report पोस्ट करण्यासाठी website वर login/signup करावे लागेल.
- फोटो upload साठी Pillow requirements मध्ये आहे.
- हा development project आहे; public production hosting करण्याआधी Django SECRET_KEY, DEBUG आणि ALLOWED_HOSTS सुरक्षितपणे configure करा.
