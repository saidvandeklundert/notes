trait Mage{
    fn cast_spell(&self);

    fn greet(&self);
}

struct FireMage{
    pub damage: i32,
    pub name: String,
}
impl Mage for FireMage{
    fn cast_spell(&self){
        println!("Firedamage {}",self.damage)
    }
    fn greet(&self){
        println!("Hello, I am {}", self.name)
    }    
}

struct IceMage{
    pub damage: i32,
    pub name: String,
}

impl Mage for IceMage{
    fn cast_spell(&self){
        println!("Icedamage {}", self.damage)
    }
    fn greet(&self){
        println!("Hello, I am {}", self.name)
    }
}


// Mage factory part

enum MageType{
    FireMage,
    IceMage,
}

struct MageFactory;
impl MageFactory{
    fn new_mage(mage_type:&MageType, name:String)-> Box<dyn Mage>{
        match mage_type{
            MageType::FireMage =>Box::new(FireMage{
                damage:32,
                name:String::from("Daar"),
            }),
            MageType::IceMage =>Box::new(IceMage{
                damage:32,
                name:String::from("Icy"),
            }),            
        }
    }
}

// Mage that has it's own factory:



fn main() {
    println!("Hello, world!");
    let fire_mage = FireMage{
        damage:32,
        name:String::from("Daar"),
    };
    fire_mage.cast_spell();
    fire_mage.greet();

    let ice_mage = IceMage{
        damage:230,
        name:String::from("Raab"),
    };
    ice_mage.cast_spell();
    ice_mage.greet();

    let factory_made = MageFactory::new_mage(
        &MageType::IceMage, String::from("Factory made")
    );
    factory_made.greet();
}
