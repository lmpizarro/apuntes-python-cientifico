import numpy as np

Barn = 10E-24
Na = 6.02e23

elements = {"U":{"dens":19.050, "mass":238.029}, 
            "Al": {"dens":2.7, "mass":26.982},
            "U235":{"dens":19.050, "mass":235.043},
            "U238":{"dens":19.050, "mass":238.050},
            }

cross_sections =  { "Al": {"fis":0,     "cap":0.231, "scat":1.413},
                   "U235":{"fis":582.0, "cap":98.8, "scat":14.020},
                   "U238":{"fis":3e-6,  "cap":2.68, "scat":9.075},
            }

class MeatUAlx_Al:

    enrich = 20.0  # percent

    dens_u = 4.4   # g*cm-3

    pc_poros = 6      # percent

    composicion = {"U235" : {"vol":0, "atoms":0},
                      "U238" : {"vol":0, "atoms":0},
                      "Al" : {"vol":0, "atoms":0}}

    macro_cross_sections = { "Al": {"fis":0, "cap":0, "scat":0.0},
                   "U235":{"fis":0.0, "cap":0.0, "scat":0.0},
                   "U238":{"fis":0.0,  "cap":0.0, "scat":0.0},
                          }

    def __init__(self, l, h, e, gU235): # l, h, e en mm
        self.l = l
        self.h = h
        self.e = e
        self.gU235 = gU235
        self.gU238 = 100 * gU235 * (1 - self.enrich / 100) / self.enrich
        self.gUtotal = self.gU235 + self.gU238
        self.vol = (l * h * e) / 1000  # cm3
        self.volPoros = (self.vol * self.pc_poros / 100)     # cm3
        self.composicion["U235"]["vol"] = self.gU235 / elements["U"]["dens"] # cm3 
        self.composicion["U238"]["vol"]= self.gU238 / elements["U"]["dens"] # cm3 
        self.volU = self.gUtotal / elements["U"]["dens"] 
        self.composicion["Al"]["vol"]= self.vol - self.volU - self.volPoros

        for k in self.composicion:
            self.composicion[k]["atoms"] = elements[k]["dens_at"]*self.composicion[k]["vol"]
            total = 0
            for l in self.macro_cross_sections[k]:
                self.macro_cross_sections[k][l] = cross_sections[k][l] *  self.composicion[k]["atoms"]
                total = total + self.macro_cross_sections[k][l]
            self.macro_cross_sections[k]["total"]  = total  


    def __repr__(self):
        en = "% enriquecimiento: "  + str(self.enrich) + "\n" 
        dn = "densidad: "  +       str(self.dens_u) + "\n"
        gu5 = "gramos u235: "  +  str(self.gU235) + "\n"
        gu8 = "gramos u238: "  +  str(self.gU238) + "\n"
        gut = "gramos utotal: "  +  str(self.gUtotal) + "\n"
        vm = "volumen del meat: " + str(self.vol) + "\n"
        vp5 = "volument U235: "  +   str(self.composicion["U235"]["vol"]) + "\n"
        vp8 = "volument U238: "  +   str(self.composicion["U238"]["vol"]) + "\n"
        vut = "volument utotal: "  +  str(self.volU) + "\n"
        vpo = "volument poros: "  +   str(self.volPoros) + "\n"
        val = "volument alloy: "  +   str(self.composicion["Al"]["vol"]) + "\n"

        return en + dn + gu5 + gu8 + gut + vm + vp5 + vp8 + vut + vpo + val

    def set_enrich(self, pc):
        self.enrich = pc

    def set_dens_u(self, dens_u):
        self.dens_u = dens_u

def init():
    print("init  densidad atomica")
    for k in elements:
        elements[k]["dens_at"] = elements[k]["dens"] * Na / elements[k]["mass"] 

    print("init  cross sections")
    for k in cross_sections:
        cross_sections[k]["cap"]=(cross_sections[k]["cap"] * Barn)
        cross_sections[k]["fis"]=(cross_sections[k]["fis"] * Barn)
        cross_sections[k]["scat"]=(cross_sections[k]["scat"] * Barn)
       
        print (k)
        print("cap", cross_sections[k]["cap"])
        print("scat", cross_sections[k]["scat"])
        print("fis", cross_sections[k]["fis"])



def init_np():
    dict_elem = {"Al": 0 , "U235": 1, "U238": 2}
    dict_cs = {"fis": 0 , "cap": 1, "scat": 2}

    a = [cross_sections["Al"]["fis"],cross_sections["Al"]["cap"],cross_sections["Al"]["scat"]]
    n_cross_sections_al = np.asarray(a)

    a = [cross_sections["U235"]["fis"],cross_sections["U235"]["cap"],cross_sections["U235"]["scat"]]
    n_cross_sections_u235 = np.asarray(a)

    a = [cross_sections["U238"]["fis"],cross_sections["U238"]["cap"],cross_sections["U238"]["scat"]]

    n_cross_sections_u238 = np.asarray(a)


    n_cross_sections = np.vstack((n_cross_sections_u238, n_cross_sections_u235,
        n_cross_sections_al   )) * Barn

    print (n_cross_sections)

    a = [elements["Al"]["dens"],elements["Al"]["mass"],  
            elements["Al"]["dens"] * Na / elements["Al"]["mass"] ]
    b = [elements["U235"]["dens"],elements["U235"]["mass"],  
            elements["U235"]["dens"] * Na / elements["U235"]["mass"] ]
    c = [elements["U238"]["dens"],elements["U238"]["mass"],  
            elements["U238"]["dens"] * Na / elements["U238"]["mass"] ]

    n_elements  = np.vstack((np.asarray(a), np.asarray(b), np.asarray(c)))

    print (n_elements)
    


if __name__ == "__main__":


    init_np()
    
    init()

    meat = MeatUAlx_Al (600, 63, 0.51, 16.957) 

    print ("hello", elements)

    print(meat.composicion)
    for k in meat.macro_cross_sections:
        print(k, meat.macro_cross_sections[k])


