let ReturnBiggerNumber = (n_1, n_2) =>{
    if (n_1 > n_2){
        return n_1;
    }
    else{
        return n_2
    }
}
first_number = parseInt(prompt("Digite o primeiro número: "));
second_number = parseInt(prompt("Digite o segundo número: "));
alert("The biggest number is: " + ReturnBiggerNumber(first_number, second_number));


let evenOrOdd = (number) => {
    if (number % 2 == 0){
        return "even"
    }
    else {
        return "odd"
    }
}
number = prompt("Digite um número:")
alert("The number is " + evenOrOdd(number));