var updateClickCount = (function() {
    var counter = 0;

    return function() {
        counter += 1; 
    };
})();