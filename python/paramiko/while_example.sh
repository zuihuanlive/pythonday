#!/bin/bash
i=1
while(($i < 4))
do
        echo '第'$i'循环'
        echo '执行所需操作'
        i=$[$i+1]
        if (($i < 4))
        then
                sleep 3
        fi
done
