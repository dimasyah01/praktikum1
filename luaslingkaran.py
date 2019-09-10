class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungluas(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   lingkaran1 = lingkaran(3.14, 57)

   print('Objek lingkaran1')
   print('phi\t: ', lingkaran1.phi)
   print('jarijari\t: ', lingkaran1.jarijari)
   print('Luas lingkaran\t= ', lingkaran1.hitungluas())

   lingkaran2 = lingkaran(3.14, 82)

   print("\nObjek lingkaran2")
   print('phi\t: ', lingkaran2.phi)
   print('jarijari\t: ', lingkaran2.jarijari)
   print("Luas lingkaran\t= ", lingkaran2.hitungluas())

if __name__ == "__main__":
   main()