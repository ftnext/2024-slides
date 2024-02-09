<?php
declare(strict_types=1);
namespace fizzbuzz;

use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

require_once __DIR__ . "/../src/fizzbuzz.php";

class FizzBuzzParametrizedTest extends TestCase
{
    public static function provide_3の倍数(): array
    {
        return [[3], [6]];
    }

    #[DataProvider("provide_3の倍数")]
    public function test_3の倍数のときはFizzを返す(int $number): void
    {
        $this->assertSame(fizzbuzz($number), "Fizz");
    }
}
