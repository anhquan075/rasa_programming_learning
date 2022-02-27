# Hệ thống chatbot hỗ trợ nhập môn lập trình
[![Build Status](https://travis-ci.com/anhquan075/cpp_learning_chatbot.svg?branch=mainbranch)](https://travis-ci.com/anhquan075/cpp_learning_chatbot)
[![Rasa 2.1.0](https://img.shields.io/badge/Rasa-2.1.0-blueviolet)](https://github.com/RasaHQ/rasa/tree/2.1.x)
[![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB)](https://www.python.org/downloads/release/python-370/)

## Hướng dẫn sử dụng:
1) Cài đặt:
- Cài đặt các thư viện cần thiết
```
pip3 install rasa[full]==2.3.2
pip3 install -r requirements.txt
```
2) Chuẩn bị dữ liệu:
- Các bạn chuẩn bị dữ liệu như trong thư mục data mà mình chuẩn bị sẵn gồm ba loại chính:
  - [NLU](https://rasa.com/docs/rasa/nlu-training-data): tại đây các bạn định nghĩa các intent và entity, trong mỗi intent và entity sẽ có một hoặc nhiều examples tương ứng.
  - [Stories](https://rasa.com/docs/rasa/stories): tại đây các bạn định nghĩa cho các cuộc hội thoại mẫu mà chat bot có thể direct người dùng theo các kịch bản tương ứng.
  - [Rules](https://rasa.com/docs/rasa/rules): một dạng khác của stories nhưng hơi bắt buộc người dùng vào các cuộc hội thoại cho trước hơn.
  - [Domain](https://rasa.com/docs/rasa/domain): khai báo các câu trả lời cho từng intent và entity nhất định.
3) Huấn luyện và kiểm thử mô hình:
- Huấn luyện:
  - Dùng lệnh ```rasa train``` để tiến hành huấn luyện mô hình, các bạn có thể tham khảo pipeline cho tiếng việt của mình dùng trong project này để huấn luyện theo. Các bạn có thể sử dụng thêm các argument trong lệnh train bằng cách gõ ```rasa train --help``` để biêt thêm thông tin chi tiết.
- Kiểm thử mô hình:
  - Đối với bộ dữ liệu ít, mình khuyên dùng:
  ```
  rasa test --cross-validation 
  ```
  - Nếu bạn có thể tạo cho mình bộ test ưng ý hoặc để kiểu thử trên chính data để dùng để train chỉ cần chạy lệnh:
  ```
  rasa test
  ```
## Docker:
Mình có tạo một tệp docker-compose để các bạn có thể chạy lại project của mình nhanh chóng và ít tốn thời gian hơn với lệnh sau:
```
docker-compose up -d
```
Sau khi creating xong 4 docker container, các bạn gõ lệnh ```docker ps``` để kiểm tra lại xem cả 4 container đã chạy chưa nhé. Container main sẽ mất thời gian một lúc để chạy nên các bạn vui lòng đợi tầm 2-3 phút nhé.

## Cấu hình tối thiểu của server để host chatbot:
- OS: Ubuntu >= 18.04
- RAM >= 8 GB
- CPU: Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz trở về sau nếu server bạn host không có GPU
- (Tùy chọn) GPU: GTX 1050Ti trở về sau vì mình dùng model transformers nên tiêu tốn khá nhiều tài nguyên.

Mọi ý kiến thắc mắc hoặc lỗi phát sinh các bạn có thể liên hệ với mình qua mail: 19522081@gm.uit.edu.vn hoặc tạo issue trực tiếp trên repo của mình.
