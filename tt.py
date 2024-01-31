"""
{% static '' %}

scp -i ~/django-portfolio-key.pem -r MyResume ubuntu@3.37.197.249:/home/ubuntu
ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249
pip install 'django<5' 'pillow<10' 'django-admin-thumbnails<0.3'

"""

ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249 rm -r /home/ubuntu/MyResume/MyPortfolio
scp -i ~/django-portfolio-key.pem -r MyPortfolio-media ubuntu@3.37.197.249:/home/ubuntu/MyResume

/MyResume/MyPortfolio/PortfolioA/posts
scp -i ~/django-portfolio-key.pem -r MyPortfolio ubuntu@3.37.197.249:/home/ubuntu/MyResume
ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249 rm -r /home/ubuntu/MyResume/MyPortfolio
nohup python3 manage.py runserver 0:80 &
pkill -9 python3