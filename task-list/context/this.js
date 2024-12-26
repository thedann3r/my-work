const blakeDoodle = {
    name: "Blake",
    breed: "Labradoodle",
    sonicAttack: "ear-rupturing atomic bark",
    mostHatedThing: "noises in the apartment hallway",
    warn: function() {
      console.log(`${this.name} the ${this.breed} issues an ${this.sonicAttack} when he hears ${this.mostHatedThing}`);
    }
  };
  blakeDoodle.warn();

