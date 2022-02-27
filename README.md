# Hệ thống chatbot hỗ trợ nhập môn lập trình
[![Build Status](https://travis-ci.com/anhquan075/cpp_learning_chatbot.svg?branch=mainbranch)](https://travis-ci.com/anhquan075/cpp_learning_chatbot)
[![Rasa 2.1.0](https://img.shields.io/badge/Rasa-2.1.0-blueviolet)](https://github.com/RasaHQ/rasa/tree/2.1.x)
[![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB)](https://www.python.org/downloads/release/python-370/)

## Hướng dẫn sử dụng:
1) Cài đặt:
- Đối với các bạn dùng anaconda:
```
conda create -n <tên env> --file requirements.txt
```
- Hoặc đơn giản hơn bạn chỉ cần chạy dòng lên sau:
```
pip3 install rasa[full]==2.2.2
```
2) Sử dụng:
- Chạy đồng thời hai lệnh sau:
```
rasa run actions
rasa run
```
3) Kiểm tra performance:
- Đối với bộ dữ liệu ít, mình khuyên dùng:
```
rasa test --cross-validation 
```
- Nếu bạn có thể tạo cho mình bộ test ưng ý hoặc để kiểu thử trên chính data để dùng để train chỉ cần chạy lệnh:
```
rasa test
```
## Docker:
- Cho các bạn thuận tiện trong việc sử dụng, mình đã build sẵn một docker image trên docker hub: 
https://hub.docker.com/repository/docker/nguyenquang7501/rasa-transformers-mmlab
- Ngoài ra, nếu các bạn muốn tự build một docker image cho riêng mình, thì thực hiện như sau:
```
docker build -t <tên image bạn muốn>:<tag của image> . ( Nhớ thêm dấu chấm nhé ;)
```
- Chờ đợi quá trình build, trong lúc đó bạn có thể lên docker hub và tạo cho mình một repo sẵn trước, nếu muốn vác image mình đi chỗ khác để sử dụng
- Để push image bạn mới tạo lên docker hub, bạn chạy lệnh như sau:
```
docker push <tên image bạn vừa tạo>:<tag của image bạn vừa tạo>
```
### Lưu ý: 
  - Tên image của bạn đặt phải trùng với tên của repo trên docker hub của bạn.
  - Nên dùng lệnh ```docker login``` đăng nhập vào tài khoản docker hub của bạn trước để tránh lỗi phát sinh.

- Để kết nối hai container chạy lệnh ```action``` và ```run``` với nhau, ta sử dụng lệnh:
```
docker create network <tên network bạn muốn tạo>
```
- Tiếp theo ta chạy lên phía bên dưới để kết nối link action server tới network ta vừa tạo:
```
docker run -d -v $(pwd)/actions:/app/actions --net <tên network bạn vừa tạo> --name <tên liên kết giữa action server và rasa> <image id của bạn> run actions
```
- Với tên liên kết giữa action server và rasa vừa tạo phía trên, ta chỉnh sửa một tí trong file endpoints.yml như sau:
```
action_endpoint:
  url: "http://<tên liên kết giữa action server và rasa>:5055/webhook"
```
- Cuối cùng ta chạy lệnh sau để kết nối 2 docker với nhau:
```
docker run -it -v $(pwd):/app -p 5005:5005 --net <tên network bạn vừa tạo> <image id của bạn> run -vv
```
### Cấu hình tối thiểu của server để host botchat ( Mình lấy cấu hình dựa theo server mình đang host botchat của mình):
- OS: Ubuntu >= 18.04 ( Khuyến khích chạy trên Ubuntu, mình chạy trên windows gặp nhiều lỗi quá nên bạn nào chạy trên windows mà bị lỗi có thể tạo issuses để mình có thể giúp nhé)
- RAM >= 8 GB
- CPU: Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz trở về sau nếu server bạn host không có GPU
- (Tùy chọn) GPU: GTX 1050Ti trở về sau vì mình dùng model transformers nên tiêu tốn khá nhiều tài nguyên.
