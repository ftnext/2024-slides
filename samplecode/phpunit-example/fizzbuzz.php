<?php
declare(strict_types=1);
function fizzbuzz(int $number): string
{
    if ($number % 3 == 0 and $number % 5 == 0) {
        return "FizzBuzz";
    } elseif ($number % 3 == 0) {
        return "Fizz";
    } elseif ($number % 5 == 0) {
        return "Buzz";
    } else {
        return "$number";
    }
}

// echo fizzbuzz(3) . "\n";
// echo fizzbuzz("5") . "\n";  // TypeError
