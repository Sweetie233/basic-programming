#!/bin/bash

# 需要在crontab文件中指定任务运行所需的所有环境变量
source /home/user/.profile
source /etc/profile
# Mode can be "local" or "remote"
MODE=$1

ROOT="/home/user/testrundir"  


MOCK_EXCH_PORT=33015  # 服务器的启动端口号


SCRIPT_DIR=$(cd $(dirname $0) 2> /dev/null && pwd -P)   #当前运行的脚本所在路径


ONLOAD_SERVER="onload --profile=$ROOT/server.opf"  
ONLOAD_CLIENT="onload --profile=$ROOT/client.opf"

function clone_or_pull
{
    path=$1 #第一个参数
    repo=$2 #第二个参数

    if [ -d "$repo" ] #如果第二个参数是一个目录
    then
        hg -R $repo pull --rebase
    else
        hg clone $path $repo
    fi
}

function no_use0
{
    clone_or_pull $M_PATH $ROOT
    clone_or_pull $BB_PATH $ROOT/bb
    clone_or_pull $SIG_PATH $ROOT/bb/signals
    clone_or_pull $FTD_PATH $ROOT/ftd
    clone_or_pull $BB_CONF_PATH $ROOT/bb-conf
}

#新建两个文件夹
if [ ! -d $ROOT/pkg ]  #-d判断如果是目录
then
    mkdir $ROOT/pkg
fi
if [ ! -d $ROOT/log ]
then
    mkdir $ROOT/log  # 存放运行的日志文件
fi


# 启动本地服务器
function start_local
{
    echo "Starting mock exchange locally..."
    cp $SCRIPT_DIR/scripts/server.opf $ROOT/server.opf
    cd $ROOT/log
    EXCH_PID=$!  # 	后台运行的最后一个进程的ID号
    sleep 1
}


function start  
{
    MODE=$1  # 本函数第一个参数
    case $MODE in
        "remote")
            start_remote $EXCH_HOST    # "start_remode" function not defined
            ;;
        "local")
            start_local
            ;;
    esac
}

# 终止exchange服务器
function stop_exchange
{
    echo "Stopping mock exchange..."
    kill $EXCH_PID
    wait $EXCH_PID
}

function stop
{
    MODE=$1
    case $MODE in
        "remote")
            stop_exchange
            ;;
        "local")  
            stop_exchange
            ;;
    esac
}

if [ $# -lt 1 ] # 如果脚本无输入参数
then
    echo "I need a parameter, \"local\" or \"remote\"?"
    echo "Script exit..."
    # echo $#
    exit
fi

start $MODE  # 执行start函数

# echo "Start Sleep..."
sleep 1  # 睡眠1秒
# echo "Sleep Done..."

for i in {1..100}
do
    printf "."
    echo $order >&3
    #echo "In loop, i = $i"
    if ! (( i % 5 ))  # 当i是5的整数时
    then
        printf "\n"
        /usr/local/bin/usleep 500000  # 延时500ms，usleep:suspend execution for microsecond intervals
    fi
done


stop $MODE # 执行stop函数，先后终止hconsole，td，exchange

echo `date +"%Y%m%d %H:%M:%S.%N"` >> $ROOT/log/timing-summary.txt

echo "-------------------------------------------"
echo "Here is the timing-summary:"
cat $ROOT/log/timing-summary.txt
