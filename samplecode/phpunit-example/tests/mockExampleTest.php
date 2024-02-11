<?php
use PHPUnit\Framework\TestCase;

require_once __DIR__ . "/../src/mockExample.php";

class MockExampleTest extends TestCase
{
    public function test_モックを使うテストの例(): void
    {
        $mocked_communication = $this->createMock(HttpCommunication::class);
        $mocked_communication->expects($this->once())
            ->method("communicate")
            ->with()
            ->willReturn(200);

        foo($mocked_communication);
    }
}
