class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungkeliling(self):
      return 2* self.phi * self.jarijari 

def main():
   lingkaran1 = lingkaran(3.14, 7)

   print('Objek lingkaran1')
   print('phi\t:', lingkaran1.phi)
   print('jarijari\t:', lingkaran1.jarijari)
   print('Keliling lingkaran\t=', lingkaran1.hitungkeliling())

   lingkaran2 = lingkaran(3.14, 3)

   print("\nObjek lingkaran2")
   print('phi\t:', lingkaran2.phi)
   print('jarijari\t:', lingkaran2.jarijari)
   print("Keliling lingkaran\t=", lingkaran2.hitungkeliling())

if __name__ == "__main__":
   main()