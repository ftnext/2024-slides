<?php

class HttpCommunication
{
    public function communicate(): int
    {
        $status_code = 200;  // ダミーの値
        echo "HTTP通信をしています...\n";
        return $status_code;
    }
}

function foo(HttpCommunication $communication): void
{
    echo "foo start\n";

    $status_code = $communication->communicate();

    echo "foo end\n";
}
