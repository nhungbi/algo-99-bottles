function bottleSong(bottle = 99) {

    if (bottle <= 0) {
      return "No more bottles of beer on the wall, no more bottles of beer.\n" + "Go to the store and buy some more, 99 bottles of beer on the wall.\n";
    }  

    if (bottle === 1) {
      return "1 bottle of beer on the wall, 1 bottle of beer\n" + "Take one down and pass it around, no more bottles of beer on the wall.\n" + "No more bottles of beer on the wall, no more bottles of beer.\n" + "Go to the store and buy some more, 99 bottles of beer on the wall.\n";
    }
    let current = `${bottle} bottles of beer on the wall, ${bottle} bottles of beer.\n` + `Take one down and pass it around, ${bottle-1} bottles of beer on the wall.\n`;
    return current + bottleSong(bottle-1);
  }
  

console.log(bottleSong(4));

