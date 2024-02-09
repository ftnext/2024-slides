<?php
declare(strict_types=1);
namespace fizzbuzz;

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
