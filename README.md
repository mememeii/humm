# Arduino 傾斜鬧鐘系統

這是一個使用 Arduino 製作的傾斜鬧鐘系統，使用伺服馬達和蜂鳴器來實現。

## 硬體需求
- Arduino Uno R3
- 伺服馬達 SG90
- 蜂鳴器
- 麵包板
- 跳線

## 接線方式
1. 伺服馬達（SG90）：
   - 紅線 → Arduino 5V
   - 棕線 → Arduino GND
   - 橙線 → Arduino 9號腳位

2. 蜂鳴器：
   - 正極（長腳）→ Arduino 8號腳位
   - 負極（短腳）→ Arduino GND

## 程式碼
```cpp
#include <Servo.h>

// 定義腳位
const int SERVO_PIN = 9;      // 伺服馬達接腳
const int BUZZER_PIN = 8;     // 蜂鳴器接腳

// 創建伺服馬達對象
Servo myservo;

// 定義角度範圍
const int START_ANGLE = 0;    // 起始角度（向上位置）
const int ALARM_ANGLE = 45;   // 警報觸發角度
const int MAX_ANGLE = 90;     // 最大角度（改為90度）

// 定義旋轉方向
bool rotatingDown = true;     // true 表示向下旋轉，false 表示向上旋轉

void setup() {
  // 初始化串口通信（用於調試）
  Serial.begin(9600);
  
  // 設置蜂鳴器腳位
  pinMode(BUZZER_PIN, OUTPUT);
  
  // 連接伺服馬達
  myservo.attach(SERVO_PIN);
  
  // 將伺服馬達移動到起始位置
  myservo.write(START_ANGLE);
}

void loop() {
  // 讀取當前角度
  int currentAngle = myservo.read();
  
  // 控制伺服馬達旋轉
  if (rotatingDown) {
    // 向下旋轉（順時針）
    if (currentAngle < MAX_ANGLE) {
      myservo.write(currentAngle + 1);
      
      // 當達到警報角度時
      if (currentAngle >= ALARM_ANGLE) {
        // 啟動蜂鳴器
        tone(BUZZER_PIN, 1000);  // 1000Hz 的聲音
        // 改變方向
        rotatingDown = false;
      }
    }
  } else {
    // 向上旋轉（逆時針）
    if (currentAngle > START_ANGLE) {
      myservo.write(currentAngle - 1);
    } else {
      // 回到起始位置
      myservo.write(START_ANGLE);
      // 停止蜂鳴器
      noTone(BUZZER_PIN);
      // 改變方向
      rotatingDown = true;
    }
  }
  
  // 延遲控制旋轉速度
  if (rotatingDown) {
    delay(50);  // 向下旋轉速度（慢）
  } else {
    delay(10);  // 向上旋轉速度（快）
  }
}
```

## 運作方式
1. 馬達從0度開始
2. 慢速順時針向下旋轉（每次增加1度，延遲50ms）
3. 當轉到45度時：
   - 蜂鳴器開始響
   - 馬達改變方向
4. 快速逆時針向上旋轉（每次減少1度，延遲10ms）
5. 回到0度時：
   - 蜂鳴器停止
   - 馬達改變方向
6. 重複以上步驟

## 可調整參數
- `ALARM_ANGLE = 45`：可以調整警報觸發的角度
- `delay(50)`：可以調整向下旋轉的速度（數值越大越慢）
- `delay(10)`：可以調整向上旋轉的速度（數值越大越慢）
- `tone(BUZZER_PIN, 1000)`：可以調整蜂鳴器的頻率（數值越大聲音越高）
