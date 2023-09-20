function PalindromePermutation(str){
    var lowercase = str.toLowerCase();
    var noSpace = lowercase.replace(/\s/g, '');
    var final = noSpace.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");

    var charCount = {};
    for(var i = 0; i < final.length; i++){
        var char = final.charAt(i);
        if(charCount[char]){
            charCount[char]++;
        } else {
            charCount[char] = 1;
        }
    }

    var oddCount = 0;
    for(var char in charCount){
        if(charCount[char] % 2 === 1){
            oddCount++;
        }
    }
    if(oddCount > 1){
        return false;
    }
    return true;
}

console.log(PalindromePermutation("Tact Coa")); // true
console.log(PalindromePermutation("kjdafjlkjdiiio")); // false
console.log(PalindromePermutation("rae bear")); // true
