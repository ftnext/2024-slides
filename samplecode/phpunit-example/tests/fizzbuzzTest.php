<?php
declare(strict_types=1);
namespace fizzbuzz;

use PHPUnit\Framework\TestCase;

require_once __DIR__ . "/../src/fizzbuzz.php";

class FizzbuzzTest extends TestCase
{
    public function test_3の倍数のときはFizzを返す(): void
    {
        $number = 3;
        $actual = fizzbuzz($number);
        $expected = "Fizz";
        $this->assertSame($actual, $expected);
    }
}
