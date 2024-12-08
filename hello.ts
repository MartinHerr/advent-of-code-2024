console.log("good night sweetie");

function example(person: Person) {
  const { name, age } = person;
  console.log(name);
}

console.log(example({ name: "martin", age: 2 }));

type Person = {
  name: string;
  age?: number;
  // dextry?: Dextry.RightHanded;
};

// function example2(name: string, surname: string) {
//   console.log(name);
// }

// enum Dextry {
//   LeftHanded = "left-handed",
//   RightHanded = "right-handed",
// }

// const test = "a" |

// const person: Person = { name: "Martin", age: 32 };

// example({ name: "coucou", age: 1 });
// example2("Martin", "Herrera");
