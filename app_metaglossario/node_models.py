
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


    # Lemma = models.CharField(max_length=256, blank=True, null=True)
    # Acronimo = models.CharField(max_length=25, blank=True, null=True)
    # Definizione = models.TextField(blank=True, null=True) # sostituire con textfield?    
    # Ambito_riferimento = models.CharField(max_length=256, blank=True, null=True)
    # Autore_definizione = models.TextField(blank=True, null=True)   
    # Posizione_definizione = models.TextField(blank=True, null=True)   
    # Url_definizione = models.URLField(max_length=400, blank=True, null=True)   
    # Titolo_documento_fonte = models.TextField(blank=True, null=True)  
    # Autore_documento_fonte = models.TextField(blank=True, null=True)   
    # Host_documento_fonte = models.TextField(blank=True, null=True)  
    # Url_documento_fonte = models.URLField(max_length=400, blank=True, null=True)
    # Commento_entry = models.TextField(blank=True, null=True)
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now().date() )
    # Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")
    # Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)

# ArrayField(models.CharField(max_length=200), blank=True)

# Tabella delle entità

class model_node(models.Model): 

    ID = models.CharField(max_length=10, primary_key=True)

    Thing = models.TextField(blank=True, null=True)

    # devo predisporre un autocompile, con una funzione def se riesco
    Entita = models.CharField(max_length=256, blank=True, null=True)


    # elementi connessi
    connected_Lemma = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    connected_Acronimo = ArrayField(models.CharField(max_length=25), blank=True, null=True)
    connected_Definizione = ArrayField(models.TextField(), blank=True, null=True)
    connected_Ambito_riferimento = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    connected_Autore_definizione = ArrayField(models.TextField(), blank=True, null=True)
    connected_Posizione_definizione = ArrayField(models.TextField(), blank=True, null=True) 
    connected_Url_definizione = ArrayField(models.URLField(max_length=400), blank=True, null=True)
    connected_Titolo_documento_fonte = ArrayField(models.TextField(), blank=True, null=True)
    connected_Url_documento_fonte = ArrayField(models.URLField(max_length=400), blank=True, null=True)
    connected_Autore_documento_fonte = ArrayField(models.TextField(), blank=True, null=True) 
    connected_Host_documento_fonte = ArrayField(models.TextField(), blank=True, null=True)
    connected_Url_documento_fonte = ArrayField(models.URLField(max_length=400), blank=True, null=True)
    connected_Commento_entry = ArrayField(models.TextField(), blank=True, null=True)
    connected_Data_inserimento_entry = ArrayField(models.DateField(),blank=False, null=False, default=timezone.now().date())
    connected_Id_statico_entry = ArrayField(models.CharField(max_length=256), blank=False, null=False, default="ITCH00000")
    connected_Admin_approval_switch = ArrayField(models.CharField(max_length=30),blank=False, null=False)
    

    class Meta:
        ordering = ['Entita', 'Thing', 'ID']

    def __str__(self):                
        return  "%s [ %s ]"  %  (self.Thing, self.ID)




