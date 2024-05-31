from django.test import TestCase
from django.urls import reverse

class PortfolioTests(TestCase):
    
    def test_portfolio_view(self):
        response = self.client.get(reverse('portfolio'))
        self.assertTemplateUsed(response, 'portfolio/portfolio.html')
        
    def test_sections(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, '<main id="about" class="current-page">')
        self.assertContains(response, '<h2 class="hdr">EDUCATION</h2>')
        self.assertContains(response, '<h2 class="experience" >EXPERIENCE</h2>')
        self.assertContains(response, '<h2 class="project1" id="project">PROJECTS</h2>')

    def test_contact_links(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, 'https://www.facebook.com/DazleSalvedia/')
        self.assertContains(response, 'https://www.instagram.com/aymdaz/')
        self.assertContains(response, 'https://t.me/Aymsheessh')
        
    def test_icon(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, '<i class="fab fa-facebook-f"></i>')
        self.assertContains(response, '<i class="fab fa-instagram"></i>')
        self.assertContains(response, '<i class="fab fa-telegram"></i>')

    def test_navigation(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, '<li><a href="#about">ABOUT</a></li>')
        self.assertContains(response, '<li><a href="#Education">EDUCATION</a></li>')
        self.assertContains(response, '<li><a href="#Experiences">EXPERIENCES</a></li>')
        self.assertContains(response, '<li><a href="#project">PROJECTS</a></li>')
        
    def test_resources(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, 'portfolio/profile1.png')
        self.assertContains(response, 'portfolio/contentbg.mp4')
        self.assertContains(response, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiJRwF_KdGtW89pSbnfyv7zvB2EANJJdplWA&s')
        self.assertContains(response, 'https://w0.peakpx.com/wallpaper/142/758/HD-wallpaper-python-logo-white-silk-texture-python-emblem-programming-language-python-silk-background.jpg')
        self.assertContains(response, 'https://i.ytimg.com/vi/A4D_6rIMDFI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLC8u5rc_imoGyl9Y7bmrVJY0xoXNw')
        self.assertContains(response, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb4w5hoyZg6AEpQYu87R2x9A8FXGqJMX_o4oMwggX73vXkv-9WjsC_ExzVbvGMePFHcUk&usqp=CAU')
        self.assertContains(response, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEmkLzfhUzYJvUj7m38lFwFNJ8owQKqOnbuQ&s')
        self.assertContains(response, 'static/portfolio/GEC.jpg')
        self.assertContains(response, 'static/portfolio/gear.jpg')
        self.assertContains(response, 'static/portfolio/lessonplan.png')
        
    def test_buttons(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, '<button class="next"><i class="fa-solid fa-arrow-right"></i></button>')
        self.assertContains(response, '<button class="prev"><i class="fa-solid fa-arrow-left"></i></button>')
        
    def test_texts(self):
        response = self.client.get(reverse('portfolio'))
        self.assertContains(response, '<span>')
        self.assertContains(response, '<p>')        
        self.assertContains(response, '<h1>') 
        self.assertContains(response, '<h2>') 
        self.assertContains(response, '<ul>') 
    