function palindrome(list){
    var firstHalf = "";
    var secondHalf = "";
    list = list.replace(/\s+/g, '');
    var size = list.length;
    var half = size / 2;
    var oddBool = false;

    if(size % 2 != 0){
        oddBool = true;
        half -= 0.5;
    }
    for(var i = 0; i < half; i++){
        if(list[i] !== ' '){
            firstHalf += list[i];
        }
    }
    for(var j = size - 1; j > half; j--){
        if(list[j] !== ' '){
            secondHalf += list[j];
        }
    }

    firstHalf = firstHalf.toLowerCase();
    //console.log("firstHalf: " + firstHalf);
    secondHalf = secondHalf.toLowerCase();
    //console.log("secondHalf: " + secondHalf);
    if(firstHalf === secondHalf){
        return true;
    }else{
        return false;
    }
}

console.log("tacocat: " + palindrome("tacocat")); // true
console.log("kjdafjlkjdiiio: " + palindrome("kjdafjlkjdiiio")); // false
console.log("draw O Coward: " + palindrome("draw O Coward")); // true
