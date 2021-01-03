from tkinter import *


class Box:

    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Test Box")
        self.win = Frame(self.root)
        self.root.geometry(f'{width}x{height}')
        self.root.configure(background='grey')
        self.root.title("Pokemon Type Checker")

        # your pokemon
        self.normal_state1 = BooleanVar()
        self.normal_box1 = Checkbutton(self.root, text="Normal", var=self.normal_state1, bg="AntiqueWhite2")
        self.normal_box1.grid(row=1, column=1)

        self.fighting_state1 = BooleanVar()
        self.fighting_box1 = Checkbutton(self.root, text="Fighting", var=self.fighting_state1, bg="red3")
        self.fighting_box1.grid(row=2, column=1)

        self.flying_state1 = BooleanVar()
        self.flying_box1 = Checkbutton(self.root, text="Flying", var=self.flying_state1, bg="light slate blue")
        self.flying_box1.grid(row=3, column=1)

        self.poison_state1 = BooleanVar()
        self.poison_box1 = Checkbutton(self.root, text="Poison", var=self.poison_state1, bg="DarkOrchid2")
        self.poison_box1.grid(row=4, column=1)

        self.ground_state1 = BooleanVar()
        self.ground_box1 = Checkbutton(self.root, text="Ground", var=self.ground_state1, bg="orange2")
        self.ground_box1.grid(row=5, column=1)

        self.rock_state1 = BooleanVar()
        self.rock_box1 = Checkbutton(self.root, text="Rock", var=self.rock_state1, bg="orange4")
        self.rock_box1.grid(row=6, column=1)

        self.bug_state1 = BooleanVar()
        self.bug_box1 = Checkbutton(self.root, text="Bug", var=self.bug_state1, bg="yellow green")
        self.bug_box1.grid(row=7, column=1)

        self.ghost_state1 = BooleanVar()
        self.ghost_box1 = Checkbutton(self.root, text="Ghost", var=self.ghost_state1, bg="dark slate blue")
        self.ghost_box1.grid(row=8, column=1)

        self.steel_state1 = BooleanVar()
        self.steel_box1 = Checkbutton(self.root, text="Steel", var=self.steel_state1, bg="seashell3")
        self.steel_box1.grid(row=9, column=1)

        self.fire_state1 = BooleanVar()
        self.fire_box1 = Checkbutton(self.root, text="Fire", var=self.fire_state1, bg="orange red")
        self.fire_box1.grid(row=1, column=2)

        self.water_state1 = BooleanVar()
        self.water_box1 = Checkbutton(self.root, text="Water", var=self.water_state1, bg="RoyalBlue1")
        self.water_box1.grid(row=2, column=2)

        self.grass_state1 = BooleanVar()
        self.grass_box1 = Checkbutton(self.root, text="Grass", var=self.grass_state1, bg="lime green")
        self.grass_box1.grid(row=3, column=2)

        self.electric_state1 = BooleanVar()
        self.electric_box1 = Checkbutton(self.root, text="Electric", var=self.electric_state1, bg="gold")
        self.electric_box1.grid(row=4, column=2)

        self.psychic_state1 = BooleanVar()
        self.psychic_box1 = Checkbutton(self.root, text="Psychic", var=self.psychic_state1, bg="deep pink")
        self.psychic_box1.grid(row=5, column=2)

        self.ice_state1 = BooleanVar()
        self.ice_box1 = Checkbutton(self.root, text="Ice", var=self.ice_state1, bg="CadetBlue2")
        self.ice_box1.grid(row=6, column=2)

        self.dragon_state1 = BooleanVar()
        self.dragon_box1 = Checkbutton(self.root, text="Dragon", var=self.dragon_state1, bg="purple3")
        self.dragon_box1.grid(row=7, column=2)

        self.dark_state1 = BooleanVar()
        self.dark_box1 = Checkbutton(self.root, text="Dark", var=self.dark_state1, bg="gray24")
        self.dark_box1.grid(row=8, column=2)

        self.fairy_state1 = BooleanVar()
        self.fairy_box1 = Checkbutton(self.root, text="Fairy", var=self.fairy_state1, bg="LightPink1")
        self.fairy_box1.grid(row=9, column=2)

        self.your_move1 = Label(self.root, text="----------Your", bg="grey")
        self.your_move1.grid(row=10, column=1)
        self.your_move2 = Label(self.root, text="Move----------      ", bg="grey")
        self.your_move2.grid(row=10, column=2)

        # their pokemon
        self.normal_state2 = BooleanVar()
        self.normal_box2 = Checkbutton(self.root, text="Normal", var=self.normal_state2, bg="AntiqueWhite2")
        self.normal_box2.grid(row=1, column=4)

        self.fighting_state2 = BooleanVar()
        self.fighting_box2 = Checkbutton(self.root, text="Fighting", var=self.fighting_state2, bg="red3")
        self.fighting_box2.grid(row=2, column=4)

        self.flying_state2 = BooleanVar()
        self.flying_box2 = Checkbutton(self.root, text="Flying", var=self.flying_state2, bg="light slate blue")
        self.flying_box2.grid(row=3, column=4)

        self.poison_state2 = BooleanVar()
        self.poison_box2 = Checkbutton(self.root, text="Poison", var=self.poison_state2, bg="DarkOrchid2")
        self.poison_box2.grid(row=4, column=4)

        self.ground_state2 = BooleanVar()
        self.ground_box2 = Checkbutton(self.root, text="Ground", var=self.ground_state2, bg="orange2")
        self.ground_box2.grid(row=5, column=4)

        self.rock_state2 = BooleanVar()
        self.rock_box2 = Checkbutton(self.root, text="Rock", var=self.rock_state2, bg="orange4")
        self.rock_box2.grid(row=6, column=4)

        self.bug_state2 = BooleanVar()
        self.bug_box2 = Checkbutton(self.root, text="Bug", var=self.bug_state2, bg="yellow green")
        self.bug_box2.grid(row=7, column=4)

        self.ghost_state2 = BooleanVar()
        self.ghost_box2 = Checkbutton(self.root, text="Ghost", var=self.ghost_state2, bg="dark slate blue")
        self.ghost_box2.grid(row=8, column=4)

        self.steel_state2 = BooleanVar()
        self.steel_box2 = Checkbutton(self.root, text="Steel", var=self.steel_state2, bg="seashell3")
        self.steel_box2.grid(row=9, column=4)

        self.fire_state2 = BooleanVar()
        self.fire_box2 = Checkbutton(self.root, text="Fire", var=self.fire_state2, bg="orange red")
        self.fire_box2.grid(row=1, column=5)

        self.water_state2 = BooleanVar()
        self.water_box2 = Checkbutton(self.root, text="Water", var=self.water_state2, bg="RoyalBlue1")
        self.water_box2.grid(row=2, column=5)

        self.grass_state2 = BooleanVar()
        self.grass_box2 = Checkbutton(self.root, text="Grass", var=self.grass_state2, bg="lime green")
        self.grass_box2.grid(row=3, column=5)

        self.electric_state2 = BooleanVar()
        self.electric_box2 = Checkbutton(self.root, text="Electric", var=self.electric_state2, bg="gold")
        self.electric_box2.grid(row=4, column=5)

        self.psychic_state2 = BooleanVar()
        self.psychic_box2 = Checkbutton(self.root, text="Psychic", var=self.psychic_state2, bg="deep pink")
        self.psychic_box2.grid(row=5, column=5)

        self.ice_state2 = BooleanVar()
        self.ice_box2 = Checkbutton(self.root, text="Ice", var=self.ice_state2, bg="CadetBlue2")
        self.ice_box2.grid(row=6, column=5)

        self.dragon_state2 = BooleanVar()
        self.dragon_box2 = Checkbutton(self.root, text="Dragon", var=self.dragon_state2, bg="purple3")
        self.dragon_box2.grid(row=7, column=5)

        self.dark_state2 = BooleanVar()
        self.dark_box2 = Checkbutton(self.root, text="Dark", var=self.dark_state2, bg="gray24")
        self.dark_box2.grid(row=8, column=5)

        self.fairy_state2 = BooleanVar()
        self.fairy_box2 = Checkbutton(self.root, text="Fairy", var=self.fairy_state2, bg="LightPink1")
        self.fairy_box2.grid(row=9, column=5)

        self.their_mon1 = Label(self.root, text="--------Their", bg="grey")
        self.their_mon1.grid(row=10, column=4)
        self.their_mon2 = Label(self.root, text="Pokemon-------       ", bg="grey")
        self.their_mon2.grid(row=10, column=5)

        self.spacer = Label(self.root, text=" vs.       ", bg="grey")
        self.spacer.grid(row=5, column=3)

        self.calc = Button(self.root, text="Calculate", command=self.show_output)
        self.calc.place(x=90, y=268)

        self.output = Text(self.root, height=1, width=20)
        self.output.place(x=190, y=270)

        self.exit = Button(self.root, text="EXIT", command=self.exit)
        self.exit.place(x=238, y=310)

    def show_output(self):
        self.output.delete(0.0, END)
        self.output.insert(END, f"{self.show_effectiveness()}x effective")

    def show_effectiveness(self):
        effectiveness = 1.0

        if self.normal_state1.get():
            if self.rock_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5
            if self.ghost_state2.get():
                effectiveness *= 0.0

        if self.fighting_state1.get():
            if self.dark_state2.get():
                effectiveness *= 2
            if self.ice_state2.get():
                effectiveness *= 2
            if self.normal_state2.get():
                effectiveness *= 2
            if self.rock_state2.get():
                effectiveness *= 2
            if self.steel_state2.get():
                effectiveness *= 2
            if self.bug_state2.get():
                effectiveness *= .5
            if self.fairy_state2.get():
                effectiveness *= .5
            if self.flying_state2.get():
                effectiveness *= .5
            if self.poison_state2.get():
                effectiveness *= .5
            if self.psychic_state2.get():
                effectiveness *= .5
            if self.ghost_state2.get():
                effectiveness *= 0.0

        if self.flying_state1.get():
            if self.bug_state2.get():
                effectiveness *= 2
            if self.fighting_state2.get():
                effectiveness *= 2
            if self.grass_state2.get():
                effectiveness *= 2
            if self.electric_state2.get():
                effectiveness *= .5
            if self.rock_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5

        if self.poison_state1.get():
            if self.fairy_state2.get():
                effectiveness *= 2
            if self.grass_state2.get():
                effectiveness *= 2
            if self.poison_state2.get():
                effectiveness *= .5
            if self.ground_state2.get():
                effectiveness *= .5
            if self.rock_state2.get():
                effectiveness *= .5
            if self.ghost_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= 0

        if self.ground_state1.get():
            if self.electric_state2.get():
                effectiveness *= 2
            if self.fire_state2.get():
                effectiveness *= 2
            if self.poison_state2.get():
                effectiveness *= 2
            if self.rock_state2.get():
                effectiveness *= 2
            if self.steel_state2.get():
                effectiveness *= 2
            if self.bug_state2.get():
                effectiveness *= .5
            if self.grass_state2.get():
                effectiveness *= .5
            if self.flying_state2.get():
                effectiveness *= 0

        if self.rock_state1.get():
            if self.bug_state2.get():
                effectiveness *= 2
            if self.fire_state2.get():
                effectiveness *= 2
            if self.flying_state2.get():
                effectiveness *= 2
            if self.ice_state2.get():
                effectiveness *= 2
            if self.fighting_state2.get():
                effectiveness *= .5
            if self.ground_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5

        if self.bug_state1.get():
            if self.dark_state2.get():
                effectiveness *= 2
            if self.grass_state2.get():
                effectiveness *= 2
            if self.psychic_state2.get():
                effectiveness *= 2
            if self.fairy_state2.get():
                effectiveness *= .5
            if self.fighting_state2.get():
                effectiveness *= .5
            if self.fire_state2.get():
                effectiveness *= .5
            if self.flying_state2.get():
                effectiveness *= .5
            if self.ghost_state2.get():
                effectiveness *= .5
            if self.poison_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5

        if self.ghost_state1.get():
            if self.ghost_state2.get():
                effectiveness *= 2
            if self.psychic_state2.get():
                effectiveness *= 2
            if self.dark_state2.get():
                effectiveness *= .5
            if self.normal_state2.get():
                effectiveness *= 0

        if self.steel_state1.get():
            if self.fairy_state2.get():
                effectiveness *= 2
            if self.ice_state2.get():
                effectiveness *= 2
            if self.rock_state2.get():
                effectiveness *= 2
            if self.electric_state2.get():
                effectiveness *= .5
            if self.fire_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5
            if self.water_state2.get():
                effectiveness *= .5

        if self.fire_state1.get():
            if self.bug_state2.get():
                effectiveness *= 2
            if self.grass_state2.get():
                effectiveness *= 2
            if self.ice_state2.get():
                effectiveness *= 2
            if self.steel_state2.get():
                effectiveness *= 2
            if self.dragon_state2.get():
                effectiveness *= .5
            if self.fire_state2.get():
                effectiveness *= .5
            if self.rock_state2.get():
                effectiveness *= .5
            if self.water_state2.get():
                effectiveness *= .5

        if self.water_state1.get():
            if self.fire_state2.get():
                effectiveness *= 2
            if self.ground_state2.get():
                effectiveness *= 2
            if self.rock_state2.get():
                effectiveness *= 2
            if self.dragon_state2.get():
                effectiveness *= .5
            if self.grass_state2.get():
                effectiveness *= .5
            if self.water_state2.get():
                effectiveness *= .5

        if self.grass_state1.get():
            if self.ground_state2.get():
                effectiveness *= 2
            if self.rock_state2.get():
                effectiveness *= 2
            if self.water_state2.get():
                effectiveness *= 2
            if self.bug_state2.get():
                effectiveness *= .5
            if self.dragon_state2.get():
                effectiveness *= .5
            if self.fire_state2.get():
                effectiveness *= .5
            if self.flying_state2.get():
                effectiveness *= .5
            if self.grass_state2.get():
                effectiveness *= .5
            if self.poison_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5

        if self.electric_state1.get():
            if self.flying_state2.get():
                effectiveness *= 2
            if self.water_state2.get():
                effectiveness *= 2
            if self.dragon_state2.get():
                effectiveness *= .5
            if self.electric_state2.get():
                effectiveness *= .5
            if self.grass_state2.get():
                effectiveness *= .5
            if self.ground_state2.get():
                effectiveness *= 0

        if self.psychic_state1.get():
            if self.fighting_state2.get():
                effectiveness *= 2
            if self.poison_state2.get():
                effectiveness *= 2
            if self.psychic_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5
            if self.dark_state2.get():
                effectiveness *= 0

        if self.ice_state1.get():
            if self.dragon_state2.get():
                effectiveness *= 2
            if self.flying_state2.get():
                effectiveness *= 2
            if self.grass_state2.get():
                effectiveness *= 2
            if self.ground_state2.get():
                effectiveness *= 2
            if self.fire_state2.get():
                effectiveness *= .5
            if self.ice_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5
            if self.water_state2.get():
                effectiveness *= .5

        if self.dragon_state1.get():
            if self.dragon_state2.get():
                effectiveness *= 2
            if self.steel_state2.get():
                effectiveness *= .5
            if self.fairy_state2.get():
                effectiveness *= 0

        if self.dark_state1.get():
            if self.ghost_state2.get():
                effectiveness *= 2
            if self.psychic_state2.get():
                effectiveness *= 2
            if self.dark_state2.get():
                effectiveness *= .5
            if self.fairy_state2.get():
                effectiveness *= .5
            if self.fighting_state2.get():
                effectiveness *= .5

        if self.fairy_state1.get():
            if self.dark_state2.get():
                effectiveness *= 2
            if self.dragon_state2.get():
                effectiveness *= 2
            if self.fighting_state2.get():
                effectiveness *= 2
            if self.fire_state2.get():
                effectiveness *= .5
            if self.poison_state2.get():
                effectiveness *= .5
            if self.steel_state2.get():
                effectiveness *= .5

        return effectiveness

    def run(self):
        self.root.mainloop()

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    box1 = Box(540, 350)
    box1.run()
