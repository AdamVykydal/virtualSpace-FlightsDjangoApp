from django.db import models

class Item(models.Model):
    nazev = models.CharField(max_length=50)
    cenaNakup = models.IntegerField()
    cenaProdej = models.IntegerField()

    def __str__(self):
        return f"nazev: {self.nazev} nákup cena: {self.cenaNakup} prodej cena:  {self.cenaProdej}"

class Customer(models.Model):
    jmeno = models.CharField(max_length=50)
    primeni = models.CharField(max_length=50)
    datumNarozeni = models.DateField(auto_now=False, auto_now_add=False)
    nakup = models.ManyToManyField(Item, blank=True, related_name="Zakaznik")

    def __str__(self):
        return f"Jmeno: {self.jmeno} Primeni: {self.primeni} Datum arození: {self.datumNarozeni} "

