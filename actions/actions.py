#from _typeshed import OpenBinaryMode
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.types import DomainDict
from datetime import datetime
from datetime import date
import calendar
import random
import requests


class CPlusPlusPractice(Action):
    def name(self) -> Text:
        return "action_cpplus_practice"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        return [SlotSet("cpplus_practice_content")]


class FlowChartPractice(Action):
    def name(self) -> Text:
        return "action_flowchart_practice_answer"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        img_url = {
            "1": "https://i.imgur.com/k8T1nBE.jpg",
            "2": "https://i.imgur.com/PSooxde.jpg",
            "3": "https://i.imgur.com/OOfikEE.jpg",
            "4": "https://i.imgur.com/SvaoVeW.jpg",
            "5": "https://i.imgur.com/VmXIWnn.jpg",
            "6": "https://i.imgur.com/S6o3vV1.jpg",
            "7": "https://i.imgur.com/OyzqVUg.jpg",
            "8": "https://i.imgur.com/tzjdhnM.jpg",
            "9": "https://i.imgur.com/FPmNkyp.jpg",
            "10": "https://i.imgur.com/dXwBstQ.jpg",
            "11": "https://i.imgur.com/Dykt9sJ.jpg",
            "12": "https://i.imgur.com/QY6bQTl.jpg",
            "13": "https://i.imgur.com/5qse2HB.jpg",
            "14": "https://i.imgur.com/Sw5juuL.jpg",
            "15": "https://i.imgur.com/R60KdEf.jpg",
            "16": "https://i.imgur.com/VIoFJxu.jpg",
            "17": "https://i.imgur.com/Re2bgsc.jpg",
            "18": "https://i.imgur.com/StFVcR3.jpg",
            "19": "https://i.imgur.com/iseYVsc.jpg",
            "20": "https://i.imgur.com/UwOga3w.jpg",
            "21": "https://i.imgur.com/GeDN41A.jpg",
            "22": "https://i.imgur.com/FjX531s.jpg",
            "23": "https://i.imgur.com/09Mp5eO.jpg",
            "24": "https://i.imgur.com/g62TVCi.jpg",
            "25": "https://i.imgur.com/1dUY7Gp.jpg",
            "26": "https://i.imgur.com/ZXjdZG9.jpg",
            "27": "https://i.imgur.com/UwuyITT.jpg",
            "28": "https://i.imgur.com/CsRhE9g.jpg",
            "29": "https://i.imgur.com/Pr41bKJ.jpg",
            "30": "https://i.imgur.com/ghiSJxM.jpg",
            "31": "https://i.imgur.com/ynZZwKz.jpg",
            "32": "https://i.imgur.com/TBvhmrp.jpg",
            "33": "https://i.imgur.com/XMWLT8p.jpg",
            "34": "https://i.imgur.com/31ueVVu.jpg",
            "35": "https://i.imgur.com/B3q8FCM.jpg",
            "36": "https://i.imgur.com/8yal7pY.jpg",
            "37": "https://i.imgur.com/gQeBYmI.jpg",
            "38": "https://i.imgur.com/vNb7JbL.jpg",
            "39": "https://i.imgur.com/BVNBsMT.jpg",
            "40": "https://i.imgur.com/ERBTqdQ.jpg",
            "41": "https://i.imgur.com/hXdulCi.jpg",
            "42": "https://i.imgur.com/pej13Kk.jpg",
            "43": "https://i.imgur.com/NoWRA7x.jpg",
            "44": "https://i.imgur.com/52D5wVW.jpg",
            "45": "https://i.imgur.com/qeqUj5s.jpg",
            "46": "https://i.imgur.com/uv3dswb.jpg",
            "47": "https://i.imgur.com/7xUKmwa.jpg",
            "48": "https://i.imgur.com/JoNNV46.jpg",
            "49": "https://i.imgur.com/26RlUm9.jpg",
            "50": "https://i.imgur.com/9Ygyw3a.jpg",
            "51": "https://i.imgur.com/2W8QEeJ.jpg",
            "52": "https://i.imgur.com/8zuBESc.jpg",
            "53": "https://i.imgur.com/WGg248P.jpg",
            "54": "https://i.imgur.com/es1D2dZ.jpg",
            "55": "https://i.imgur.com/fMjerxC.jpg",
            "56": "https://i.imgur.com/zRAfpR9.jpg",
            "57": "https://i.imgur.com/VBDQedP.jpg",
            "58": "https://i.imgur.com/wNF9scm.jpg",
            "59": "https://i.imgur.com/OwXQ35H.jpg",
            "60": "https://i.imgur.com/ts7ikFo.jpg",
            "61": "https://i.imgur.com/AjQ0s6E.jpg",
            "62": "https://i.imgur.com/Xr3IuNC.jpg",
            "63": "https://i.imgur.com/bW3Zr9a.jpg",
            "64": "https://i.imgur.com/KHe9m2r.jpg",
            "65": "https://i.imgur.com/IanIKbk.jpg",
            "66": "https://i.imgur.com/CabxaSo.jpg",
            "67": "https://i.imgur.com/91oSikV.jpg",
            "68": "https://i.imgur.com/FECjYx7.jpg",
            "69": "https://i.imgur.com/wXejgvr.jpg",
            "70": "https://i.imgur.com/yl64Hcr.jpg",
            "71": "https://i.imgur.com/8zNl9ym.jpg",
            "72": "https://i.imgur.com/rG8gi1M.jpg",
            "73": "https://i.imgur.com/MtU9h2R.jpg",
            "74": "https://i.imgur.com/Six00jV.jpg",
            "75": "https://i.imgur.com/M4MC1yD.jpg",
            "76": "https://i.imgur.com/124sRvx.jpg",
            "77": "https://i.imgur.com/y7BN56G.jpg",
            "78": "https://i.imgur.com/8OqIpYF.jpg",
            "79": "https://i.imgur.com/cCVCXKU.jpg",
            "80": "https://i.imgur.com/XwwV0M8.jpg",
            "81": "https://i.imgur.com/aXGKhEt.jpg",
            "82": "https://i.imgur.com/7hRNfZu.jpg",
            "83": "https://i.imgur.com/6OzcmLu.jpg",
            "84": "https://i.imgur.com/VWHBY36.jpg",
            "85": "https://i.imgur.com/yZpfJJT.jpg",
            "86": "https://i.imgur.com/Mpq97ih.jpg",
            "87": "https://i.imgur.com/4CIFhQn.jpg",
            "88": "https://i.imgur.com/FMThsjz.jpg",
            "89": "https://i.imgur.com/gNuL1xI.jpg",
            "90": "https://i.imgur.com/I32YcqL.jpg",
            "91": "https://i.imgur.com/IHghLrt.jpg",
            "92": "https://i.imgur.com/kMblXuS.jpg",
            "93": "https://i.imgur.com/j9q2d8M.jpg",
            "94": "https://i.imgur.com/Rpjr0Eu.jpg",
            "95": "https://i.imgur.com/FRSC0uL.jpg",
            "96": "https://i.imgur.com/ordgtXk.jpg",
            "97": "https://i.imgur.com/B8Ts5wt.jpg",
            "98": ''' ''',
            "99": ''' ''',
            "100": ''' '''
        }
        quest_num = tracker.get_slot("flowchart_quest_num")
        flowchart_question_answer = " "
        print(quest_num)

        response = requests.get('https://api.giphy.com/v1/gifs/search?q=sorry&api_key=L8F3EHEDIRlvniQyJju5iYsPzX6PN94c&limit=100').json()

        if(type(quest_num) == list):
            try:
                for entity in quest_num:
                    entity = str(entity)
                    if img_url[entity] == ''' ''':
                        flowchart_question_answer = response['data'][random.randint(1,50)]['images']['original']['url']
                        dispatcher.utter_message(text='Sorry this service is not available')
                        dispatcher.utter_message(image=flowchart_question_answer)
                    else:
                        flowchart_question_answer = img_url[entity]
                        dispatcher.utter_message(text=f'Lưu đồ thuật toán bài {entity}:')
                        dispatcher.utter_message(image=flowchart_question_answer)
            except:
                flowchart_question_answer = response['data'][random.randint(1,50)]['images']['original']['url']
                dispatcher.utter_message(text='Sorry this service is not available')
                dispatcher.utter_message(image=flowchart_question_answer)
        else:
            try:
                quest_num = str(quest_num)
                if img_url[quest_num] == ''' ''':
                    flowchart_question_answer = response['data'][random.randint(1,50)]['images']['original']['url']
                    dispatcher.utter_message(text='Sorry this service is not available')
                    dispatcher.utter_message(image=flowchart_question_answer)
                else:
                    flowchart_question_answer = img_url[quest_num]
                    dispatcher.utter_message(text=f'Lưu đồ thuật toán bài {quest_num}:')
                    dispatcher.utter_message(image=flowchart_question_answer)
            except:
                flowchart_question_answer = response['data'][random.randint(1,50)]['images']['original']['url']
                dispatcher.utter_message(text='Sorry this service is not available')
                dispatcher.utter_message(image=flowchart_question_answer)
        
        return [SlotSet("flowchart_answer", flowchart_question_answer if flowchart_question_answer is not None else [])]

    
class AnswerCppDefineQuestion(Action):

    def name(self) -> Text:
        return "action_cpplus_content_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cpp_content = tracker.get_slot("cpplus_content")

        curr_intent = tracker.latest_message['intent'].get('name')
        print("Entity extracted: ", cpp_content)
        
        # Dict for answers what

        all_answers_what = {
            'comment': "Comment là một dòng hoặc nhiều dòng văn bản, được chèn vào source code chương trình, nhằm làm cho source code trở nên dễ hiểu hơn với người đọc, được bỏ qua bởi compiler và interpreter.",
            'cplusplus': '''Ngôn ngữ C++ được Bjarne Stroustrup phát triển từ ngôn ngữ C từ cuối thập niên 1970.
             _ C++ là một phiên bản mở rộng của ngôn ngữ C, kết hợp tất cả các tính năng đã có của C.
             _ C++ được coi như là ngôn ngữ bậc trung (middle-level), kết hợp các đặc điểm và tính năng của ngôn ngữ bậc cao và bậc thấp.
             _ C++ có thể dùng để lập trình nhúng, lập trình hệ thống, hoặc những ứng dụng, game…
             _ C++ là ngôn ngữ "đa hướng". Nghĩa là nó hướng cấu trúc giống C và có thêm một tính năng cực kỳ quan trọng đó là tính năng hướng đối tượng. Các bạn sẽ được học phần hướng đối tượng của C++ trong serial Lập trình hướng đối tượng C++.
             _ C++ là một trong những ngôn ngữ lập trình phổ biết trên thế giới.
             ''',
            'include': 'Include (Tạm dịch: Bao gồm) là một từ khóa trong C++ dùng để chỉ cho trình biên dịch biết rằng chúng ta cần sử dụng thư viện được khai báo và nó sẽ tự động thêm vào cho chúng ta. Cú pháp: #include <library_name>',
            'library': 'Library (Tạm dịch: Thư viện) là một tập mã nguồn đã được đóng gói, có thể được tái sử dụng trong nhiều chương trình khác nhau.',
            'namespace': 'Namespace (Tạm dịch: Không gian tên) là một từ khóa trong C++ được sử dụng để định nghĩa một phạm vi nhằm mục đích phân biệt các hàm, lớp, biến, ... cùng tên trong các thư viện khác nhau.',
            'pseudo-code': 'Pseudo code (Tạm dịch: Mã giả) là một bản mô tả giải thuật lập trình máy tính ngắn gọn và không chính thức cấp cao, trong đó sử dụng những quy ước có cấu trúc của một số ngôn ngữ lập trình, nhưng thường bỏ đi những chi tiết không cần thiết để giúp hiểu rõ giải thuật hơn.',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': "Variable (Tạm dịch: Biến) trong C++ là là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin. Bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.",
            'unsigned': '''Unsigned (Tạm dịch: Không dấu) trong C++ là một kiểu dữ liệu số nguyên không dấu, chỉ cho phép ta chứa các số nguyên không âm. Điểm khác biệt giữa unsigned và int đó là miền giá trị của chúng!
              Việc khai báo unsigned <var_name> cũng sẽ tương tự như việc khai báo unsigned int <var_name>''',
            'signed': '''Signed (Tạm dịch: Có dấu) trong C++ là một kiểu dữ liệu số nguyên có dấu, cho phép ta chứa các giá trị âm hoặc dương!
             Việc khai báo signed <var_name> cũng sẽ tương tự như việc khai báo int <var_name>, signed int <var_name>.''',
            'short': '''Short (Tạm dịch: Ngắn) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các số -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của short so với int nằm ở việc có miền giá trị nhỏ hơn!''',
            'long': 'Long (Tạm dịch: Dài) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các giá trị -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của long so với int nằm ở việc có miền giá trị to hơn!',
            'type-modififer': 'Type modifiers hay Modifers (Tạm dịch: Công cụ chỉnh sửa kiểu dữ liệu) trong C++ là các từ khóa đứng trước các kiểu dữ liệu cơ bản, làm thay đổi các tính chất mặc định của chúng như miền giá trị,... Trong C++ gồm có 4 modifers đó là: unsigned, signed, short và long.',
            'typedef': '''Typedef (Tạm dịch: Định nghĩa kiểu dữ liệu) trong C++ là một từ khóa cho phép ta định nghĩa thêm tên mới cho các kiểu dữ liệu có sẵn.
            _ Cú pháp như sau: typedef <data_type> <new_name>''',
            'constant': 'Constant hay const (Tạm dịch: Hằng số) trong C++ là một từ khóa dùng để chỉ định một biến hay một đối tượng (trong OOP) là một hằng - tức không thể làm thay đổi giá trị của nó kể từ sau khi khai báo từ khóa const.',
            'macro': '''Macro trong C++ là một trong các chỉ thị trong bộ tiền xử lý (Preprocessing), dùng để đặt lại tên của một chức năng, khối lệnh, giá trị,... theo ý của mình.
            _ Cú pháp: #define <new_name> <a syntax, code block,...> 
            _ Mình cũng có ví dụ như sau, giả sử mình muốn định nghĩa giá trị 3.14 có tên gọi là PI, mình có thể sử dụng macro như sau: #define PI 3.14''',
            'wchar-t': 'wchar-t trong C++ là một kiểu dữ liệu wide character. Wide character khá giống với kiểu char ngoại trừ việc nó chiếm gấp đôi bộ nhớ và có thể một giá trị lớn hơn kiểu char (> 256)',
            'boolean': 'Boolean hay bool (Tạm dịch: Kiểu luận lý) trong C++ là một kiểu dữ liệu đại số luận lý chỉ gồm có hai giá trị là 0 (false) và 1 (true).',
            'data-type': 'Data type (Tạm dịch: Kiểu dữ liệu) trong C++ là một hệ thống dùng để phân biệt sự khác nhau về lượng tài nguyên chiếm trong bộ nhớ và cách diễn giải mẫu bit của các biến hoặc các hàm.',
            '2d-array':'''Two dimensional array (Tạm dịch: Mảng hai chiều) là một cấu trúc dữ liệu có dạng là một bảng các số - tức là một ma trận (tìm hiểu thêm về Đại số tuyến tính để hiểu rõ hơn nhé) bao gồm n hàng và n cột.
            _ Cú pháp: <data_type> <variable_name>[<row_size>][<column_size>];''',
            'array':'''Array (Tạm dịch: Mảng) trong C++ là một kiểu dữ liệu, gồm một tập hợp các phần tử có cùng kiểu dữ liệu với nhau, được phân biệt bởi số thứ tự (index) bên trong mảng, bắt đầu từ vị trí 0.
            _ Cú pháp: <data_type> <variable_name>[<size_of_array>];''',
            'structure': '''Structure hay struct (Tạm dịch: Cấu trúc) trong C++ là một cú pháp dùng để biểu diễn một kiểu dữ liệu mới dựa vào việc tập hợp các biến cần thiết với nhau.
            _ Cú pháp: struct <name>{
                //some variables;
            };''',
            'class': '''Class (Tạm dịch: Lớp) trong C++ là một kiến thức liên quan đến Lập trình hướng đối tượng (Object Oriented Programming), là một bản thiết kế của các đối tượng có cùng chung các đặc điểm, tính chất, hành vi... Trong lập trình, một class có thể chứa các Biến - Thuộc tính (Attributes) và các Hàm - Phương thức (Methods). 
            _ Cú pháp: class <class_name>{
                //Some attributes
                //Some methods
            };
            _ Để có thể hiểu rõ hơn về Class, bạn hãy tìm hiểu thêm về Lập trình hướng đối tượng nhé!''',
            'union': '''Union (Tạm dịch: Hợp nhất) trong C++ là một cú pháp về cơ bản giống với struct, dùng để gom nhóm các biến lại với nhau để từ đó hình thành một kiểu dữ liệu mới.
            _ Cú pháp: union <union_name>{
                //some variables
            };''',
            'pointer': '''Pointer (Tạm dịch: Con trỏ) trong C++ là một biến chứa địa chỉ của một biến khác với cùng kiểu dữ liệu đã được khai báo.
            _ Cú pháp: <data_type>* <variable_name>;''',
            'enumeration': 'Enumeration hay enum (Tạm dịch: Kiểu liệt kê) là một kiểu dữ liệu trong C++ dùng để định nghĩa một tập các hằng số cố định,',
            'integer': '''Integer hay int (Tạm dịch: Kiểu số nguyên) trong C++ là một kiểu dữ liệu cho phép lưu trữ những giá trị là số nguyên như -2,-1,0,1,...
            _ Cú pháp: int <variable_name>;''',
            'floating-point': '''Floating point hay float (Tạm dịch: Kiểu dấu chấm động/kiểu số thực) trong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... Nói cách khác, kiểu dấu chấm động cho phép ta lưu trữ cả phần thập phân của một số.
            _ Cú pháp: float <variable_name>;''',
            'double': '''Double trong C++ là một kiểu dữ liệu ctrong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... giống như kiểu float. Điểm khác biệt của double so với float nằm ở việc có miền giá trị lớn hơn.
            _ Cú pháp: double <variable_name>;''',
            'character': '''Character hay char (Tạm dịch: Kiểu kí tự) trong C++ là một kiểu dữ liệu dùng để lưu trữ một ký tự trong bảng mã ASCII như 1,2,3,a,b,c,d,... Kiểu char còn đặc biệt ở chỗ, nó vừa là kiểu kí tự nhưng cũng vừa là kiểu số nguyên (integer), chính vì thế ta cũng thể sử dụng số để đại diện cho các kí tự theo bảng mã ASCII khi làm việc với kiểu char.
            _ Cú pháp: char <variable_name>;''',
            'string': '''String (Tạm dịch: Kiểu chuỗi kí tự) trong C++ là một kiểu dữ liệu tập hợp các kí tự được đặt trong dấu ngoặc kép, dùng để biểu diễn một đoạn văn bản,... Lưu ý rằng kiểu string không phải là một kiểu dữ liệu được dựng sẵn trong C++ mà nó được cài đặt trong thư viện STL, vì vậy để sử dụng được string trước tiên các bạn cần phải khai báo: #include <string> cái đã nha!
            _ Cú pháp: std::string <variable_name>;''',
            'local-variable': '''Local variables (Tạm dịch: Biến cục bộ) trong C++ là một biến được định nghĩa bên trong một khối lệnh.''',
            'global-variable': '''Global variables (Tạm dịch: Biến toàn cục) trong C++ theo quy ước được khai báo ở đầu của một tập tin, bên dưới #include. Chính vì được khai báo ngay đầu tập tin mà không nằm trong phạm vi của một khối lệnh nào nên biến toàn cục - đúng với tên gọi của nó sẽ có phạm vi hoạt động là toàn bộ tập tin code, tức là ta có thể sử dụng nó ở bất kì đâu mà ta muốn.''',
            'auto': 'Auto (Tạm dịch: Tự động) trong C++ 11 là một kiểu dữ liệu cho phép nhận diện kiểu dữ liệu của một biến thông qua giá trị ta khởi tạo nó, ví dụ nếu ta khai báo: auto aStr = 10; thì kiểu dữ liệu của aStr lúc này sẽ là kiểu int',
            'external': '''External Variables (Tạm dịch: Biến ngoại) là biến mà có thể dùng chung ở các sourcefile khác nhau. Để có thể khai báo external variables, ta cần phải sử dụng từ khóa extern khi khai báo biến, và việc khai báo các external variables nên được thực hiện ở các header file (file .h) để tiện sử dụng.''',
            'static': '''Static (Tạm dịch: Tĩnh) trong C++ là một từ khóa có thể sử dụng để khai báo chung với biến, hàm hoặc các thuộc tính, phương thức trong một class (OOP). Với biến static, dù đặt bên trong hay bên ngoài khối lệnh thì nó vẫn sẽ có hiệu lực - tức bất kì sự thay đổi giá trị ở đâu cũng làm biến static cập nhật đúng với giá trị đó - giống với Biến toàn cục (Global variable).''',
            'vector': '''Vector trong C++ là một đối tượng có thể chứa một chuỗi các vùng nhớ liên tiếp nằm trong thư viện STL, đại diện cho kiểu Mảng (Array) thông thường. Khá giống với kiểu Mảng về chức năng, nhưng bên cạnh đó Vector còn cho thấy thêm một số điểm ưu việt hơn so với Array như việc không cần phải khai báo kích thước vì Vector có thể tự động tăng kích thước của nó lên, có thể biết được số lượng phần tử đang lưu bên trong nó hay có thể dùng được số phần tử âm,...''',
            'reference-variable': '''Reference variables (Tạm dịch: Biến tham chiếu) là một biến có các đặc điểm sau đây:
            + _Biến tham chiếu không được cấp phát bộ nhớ, không có địa chỉ riêng.
            + _Nó dùng làm bí danh cho một biến (kiểu giá trị) nào đó và nó sử dụng vùng nhớ của biến này.
            Cú pháp: <data_type> &<variable_name> = <any_declared_variable>;''',
            # Câu trả lời về các toán tử
            'decrement-operator': '''Decrement operators (Tạm dịch: Toán tử giảm, Ký hiệu: --) là loại toán tử giảm giá trị của biến xuống 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix decrement (Đứng trước biến): giảm giá trị của biến lên trước rồi cập nhật giá trị mới vào biến ngay lập tức.\n
             _ Postfix decrement (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã giảm 1)''',
            'increment-operator': '''Increment operators (Tạm dịch: Toán tử tăng, Ký hiệu: ++) là loại toán tử tăng giá trị của biến lên 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix increment (Đứng trước biến): tăng giá trị của biến lên trước rồi cập nhật giá trị mới vào x ngay lập tức.\n
             _ Postfix increment (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã tăng 1)''',
            'dereference-operator': '''Dereference operators (Tạm dịch: Toán tử trỏ, Ký hiệu: *) là loại toán tử cho phép chúng ta truy cập vào giá trị tại một địa chỉ cụ thể.''',
            'address_of-operator': '''Address_of operators (Tạm dịch: Toán tử địa chỉ, Ký hiệu : &) là loại toán tử cho phép chúng ta lấy địa chỉ bộ nhớ của một biến.''',
            'comma-operator': '''Comma operator (Tạm dịch: Toán tử phẩy, Ký hiệu : ,) là một loại toán tử cho phép ta kết nối các biểu thức lại với nhau, thực thi theo trình tự từ trái sang phải.''',
            'ternary-operator': '''Ternary operators (Tạm dịch: Toán tử ba ngôi, Ký hiệu: ? :) là toán tử có 3 toán hạng trong biểu thức. Cú pháp: (<condition_expression>) ? <value_if_true> : <value_if_false);
             Trong đó: 
             + _condition_expression: là một biểu thức điều kiện kiểu bool, thứ sẽ quyết định kết quả của phép toán.
             + _value_if_true: Nếu biểu thức điều kiện trả về true, đây là sẽ là kết quả của phép toán.
             + _value_if_false: Nếu biểu thức điều kiện trả về false, đây là sẽ kết quả của phép toán.''',
            'binary-operator': 'Binary operators (Tạm dịch: Toán tử hai ngôi) là toán tử có 2 toán hạng trong biểu thức. Có 5 toán tử số học 2 ngôi trong C++ đó là: Cộng (Addition : +), Trừ (Subtraction : -), Nhân (Multiplication : *), Chia lấy nguyên (Division : /), Chia lấy dư (Modulus : %)',
            'unary-operator': 'Unary operators (Tạm dịch: Toán tử một ngôi) là toán tử chỉ có 1 toán hạng trong biểu thức. Ví dụ như việc bạn sử dụng dấu - để biểu diễn số âm kiểu -11, -60,...',
            'shift-operator': 'Shift operators (Tạm dịch: Toán tử dời bit) bao gồm toán tử dời qua phải (right-shift - >>) và toán tử dời qua trái (left-shift - <<).',
            'bitwise-operator': '''Bitwise operators (Tạm dịch: Toán tử bit) là toán tử họa động trên các bits và thực hiện các phép toán liên quan đến bit như &(AND), |(OR), ^(XOR), ~(One's complement), <<(Left shift), >>(Right shift).''',
            'logical-operator': 'Logical operators (Tạm dịch: Toán tử logic) là loại toán tử dùng để kết hợp hai hay nhiều điều kiện lại với nhau để đánh giá và đưa ra kết quả cuối cùng. Ta có toán tử AND (&& - chỉ đúng khi tất cả điều kiện đều đúng), toán tử OR (|| - chỉ đúng khi một trong các điều kiện là đúng) và toán tử NOT(! - chỉ đúng khi kết quả cuối cùng của biểu thức là sai)',
            'comparison-operator': 'Comparison operators hay Relational operators (Tạm dịch: Toán tử so sánh) là loại toán tử cho phép thực hiện các phép toán so sánh như so sánh hơn, so sánh bằng,...',
            'arithmetic-operator': 'Arithmetic operators (Tạm dịch: Toán tử số học) là loại toán tử dùng để biểu diễn các phép toán số học như +,-,*,/,%...',
            'assignment-operator': 'Assignment Operators (Tạm dịch: Toán tử gán, Ký hiệu: =) là một loại toán tử dùng để cấp phát giá trị',
            'operator': 'Operators (Tạm dịch: Toán tử) trong lập trình là một biểu tượng đại diện cho các phép toán số học như cộng trừ nhân chia hay các phép toán logic,... và trả về một kết quả. Trong C++, có rất nhiều loại toán tử nhưng cơ bản và chung nhất, ta có thể chia toán tử làm ba loại: Toán tử một ngôi (Unary Operator), Toán tử hai ngôi (Binary Operator) và Toán tử ba ngôi (Ternary Operator).',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': '''If hay If statements (Tạm dịch: Lệnh if) là một lệnh được dùng để kiểm tra một biểu thức kiểu luận lý nào đó là đúng hay sai, nếu đúng thì sẽ thực thi tập chỉ thị bên trong khối if, nếu điều kiện sai thì sẽ bỏ qua khối lệnh if đó.\n
            Cú pháp: 
            if(<boolean_expression>){
                //some codes here...
            }
            Chi tiết hơn, Lệnh if còn được phân loại thành 4 loại: if, if else, if else if Ladder và nested if''',
            'loop': 'Loop (Tạm dịch: Sự lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop).',
            'control-flow': 'Control flow hay Flow of control (Tạm dịch: Cấu trúc điều khiển) trong lập trình là một khái niệm dùng để chỉ một tập các chỉ thị, các lệnh hay các lời gọi hàm được thực thi khi chạy chương trình.',
            'selection-statement': 'Selection statements (Tạm dịch: Lệnh lựa chọn) trong lập trình là một khái niệm dùng để chỉ sự quyết định thực thi một tập các chỉ thị hay một khối lệnh dựa dựa trên một điều kiện cho trước. Trong C++, ta có thể dùng lệnh if hoặc lệnh switch để có thể sử dụng lệnh lựa chọn.',
            'iteration-statement': 'Iteration statements hay Loop (Tạm dịch: Lệnh lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop)',
            'jump-statement': 'Jump statements (Tạm dịch: Lệnh nhảy) trong lập trình là một khái niệm dùng để chỉ sự làm thay đổi đột ngột hướng thực thi code một cách vô điều kiện sang một tập chỉ khác ở một nơi nào đó trong tập tin code của chúng ta. Trong C++, ta có thể biểu diễn Lệnh nhảy bằng các lệnh gồm Lệnh break, Lệnh continue, Lệnh goto và Lệnh return.',
            'for': '''For hay For loops (Tạm dịch: Vòng lặp for) trong C++ là một cấu trúc vòng lặp với chức năng tương tự như vòng while nhưng khác về cú pháp.
             Cấu trúc của một vòng for như sau:
            for(<loop_variable_declaration>;<stop_condition_expression>;<update_loop_variable_expression>){
                //Some codes here...
             }
             Với:
             _ loop_variable_declation: là nơi khởi tạo biến lặp, biến lặp được sử dụng như là một máy đếm số lần đã lặp của vòng for.
             _ stop_condition_expression: là nơi khởi tạo một biểu thức kiểu bool cho biến lặp, khi không còn thỏa mãn biểu thức này (false) thì vòng lặp sẽ kết thúc.
             _ update_loop_variable_expression: là nơi khởi tạo một biểu thức để cập nhật giá trị cho biến lặp sau mỗi lần lặp.''',
            'while': '''While hay While loops (Tạm dịch: Vòng lặp while) trong C++ là một vòng lặp với chức năng tương tự như vòng for nhưng khác về cú pháp. Cấu trúc của một vòng while như sau:
             while(<condition_expression>){
                 //some codes here...
            }
            Mình thể hiểu đơn giản cấu trúc đó như sau: trong khi điều kiện <condition_expression> vẫn trả về kết quả đúng (true), thì các đoạn code bên trong dấu { } vẫn sẽ được thực thi.''',
            'do-while': '''do while (Tạm dịch: Vòng lặp do while) trong C++ là một vòng lặp khá giống với vòng lặp while, điểm khác biệt ở do while so với while là nó sẽ đảm bảo vòng lặp sẽ được lặp ít nhất một lần.Cú pháp:\n
             do {
                // Some codes here;
            } while (<condition_expression>);''',
            'switch': '''Switch statements (Tạm dịch: Lệnh chuyển mạch) trong C++ giống như là một chuỗi các câu lệnh if else với việc so sánh một biến với các số nguyên. Cú pháp:
             switch (n)
            {
                case 1: // Sẽ thực thi khối lệnh ở đây nếu n == 1;
                        break;
                case 2: // Sẽ thực thi khối lệnh ở đây nếu n == 2;
                        break;
                default: // Nếu n không bằng với bất kì case nào thì sẽ thực thi khối lệnh ở đây;
            }''',
            'break': 'Break statements (Tạm dịch: Lệnh chấm dứt) trong C++ là một trong các lệnh nhảy, dùng để kết thúc một vòng lặp ngay lập tức kể cả khi nó vẫn còn có thể tiếp tục lặp.',
            'continue': 'Continue statements (Tạm dịch: Lệnh tiếp tục) trong C++ là một trong các lệnh nhảy, dùng để ép buộc trình biên dịch phải nhảy đến lần lặp kế tiếp của một vòng lặp.',
            'goto': '''Goto statements (Tạm dịch: Lệnh goto) trong C++ là một trong các lệnh nhảy, dùng để thực hiện việc đẩy trình biên dịch đến một đoạn code khác (label) và thực thi chúng. Cú pháp:
             // some code heres...;
             goto <label_name>;
            
             <label_name>:
             // some codes here;''',
            'if-else': '''if else (Tạm dịch: Nếu không thì...) là một dạng đặc biệt của lệnh if khi mà ta có thể định nghĩa thêm một khối lệnh cho trường hợp biểu thức điều kiện sai.''',
            'if-else-if-ladder': '''if else if Ladder (Tạm dịch: Cầu thang if else) là một dạng đặc biệt của lệnh if khi ta định nghĩa thêm nhiều lệnh if hơn sau mỗi else.''',
            'nested-if': '''Nested if (Tạm dịch: if lồng if) là một dạng đặc biệt của lệnh if khi bên trong khối lệnh if lại có thêm một khối if khác nữa.Ví dụ như sau:''',
            # Câu trả lời về function
            'function': 'Function (Tạm dịch: Hàm) là một đoạn các câu lệnh có thể tái sử dụng. Function cho phép lập trình viên cấu trúc chương trình thành những phân đoạn khác nhau để thực hiện những công việc khác nhau.',
            'parameter': 'Parameters (Tạm dịch: Tham số) là những gì chúng ta gọi khi định nghĩa một hàm. Parameter sẽ đại diện cho một giá trị mà hàm của bạn sẽ nhận được khi được gọi.',
            'argument': 'Arguments (Tạm dịch: Đối số) là đại diện cho giá trị truyền cho parameter khi chúng ta thực hiện lời gọi hàm. Mỗi argument sẽ tương ứng với một parameter khi khai báo.',
            'recursion': 'Recursion (Tạm dịch: Đệ quy) là một hàm tự gọi lại chính nó.',
            'pass-by-value': 'Pass by value (Tạm dich: Truyền tham trị) có thể được hiểu là giá trị của biến sẽ không bị thay đổi khi ta truyền biến này vào một hàm mà trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'pass-by-reference': 'Pass by reference (Tạm dịch: Truyền tham chiếu) có thể được hiểu là giá trị của biến sẽ bị thay đổi khi ta truyền biến này vào một hàm trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'return': 'Return keyword (Tạm dịch: Trả về) trong C++ là một từ khóa dùng để trả về một giá trị cho nơi gọi hàm, đây từ khóa bắt buộc đối với bất kì hàm nào được khai báo có giá trị trả về, và có thể có hoặc không đối với hàm khai báo kiểu void.',
            'return-type': 'Return type (Tạm dịch: Kiểu trả về của hàm) trong C++ là việc định nghĩa kiểu giá trị mà hàm đó sẽ trả về cho nơi gọi hàm, giả sử ta khai báo một hàm kiểu int thì khi thực hiện lời gọi hàm, hàm này chắc chắn sẽ trả về một giá trị int.',
            'const-reference': 'Const reference (Tạm dịch: Tham chiếu hằng) trong C++ là việc ta định nghĩa tham số truyền vào là tham chiếu với từ khóa const - tức là sẽ không thể thay đổi được giá trị của biến truyền vào hàm mặc dù đó là tham chiếu. Hiệu quả của việc sử dụng tham chiếu hằng chỉ thể hiện rõ khi làm việc với các đối tượng struct/class.',
            'inline-function': 'Inline functions (Tạm dịch: Hàm nội tuyến) là một loại hàm trong ngôn ngữ lập trình C++. Từ khoá inline được sử dụng để đề nghị (không phải là bắt buộc) compiler (trình biên dịch) thực hiện inline expansion (khai triển nội tuyến) với hàm đó hay nói cách khác là chèn code của hàm đó tại địa chỉ mà nó được gọi.',
            'default-value': 'Default values (Tạm dịch: Tham số mặc nhiên) là khi ta mặc định gán sẵn giá trị bất kì cho một tham số truyền vào khi thực hiện khai báo hàm. Điều đó đồng nghĩa, khi thực hiện lời gọi hàm mà không truyền vào đối số tương ứng, trình biên dịch sẽ sử dụng giá trị đã được gán sẵn cho tham số đó khi thực thi hàm.',
            'main-function': 'Main function (Tạm dịch: Hàm main) trong C++ là một trường hợp của hàm, đây là nơi sẽ được thực thi đầu tiên khi chạy một chương trình C++.',
            'built-in-function': '''Built in functions (Tạm dịch: Hàm dựng sẵn) hay còn có tên gọi khác là Library functions, là các hàm ta có thể gọi nó trực tiếp mà không cần phải khai báo và định nghĩa chúng bởi vì chúng đã được viết sẵn trong các thư viện của C++ như thư viện stdio.h, iostream,...''',
            'lambda':'''Lambda function (Tạm dịch: Hàm vô danh) là hàm dùng để truyền vào 1 hàm khác và sử dụng 1 lần.''',
            'flowchart':'''Lưu đồ thuật toán (Flowchart) là một loại sơ đồ biểu diễn một thuật toán hoặc một quá trình, biểu hiện các bước công việc dưới dạng các loại hình hôp khác nhau theo thứ tự được biểu diễn bởi các mũi tên. Sơ đồ này có thể thể hiện giải pháp cho vấn đề cần giải quyết từng bước từng bước một. Các bước quá trình được hiển thị dưới dạng các hình hộp được nối với nhau bằng các mũi tên để thể hiện dòng điều khiển.''',
            'introduction-to-programming': '''Nhập môn lập trình (Introduction to programming) là một môn học về tin học-lập trình gần như là bắt buộc đối với tất cả các sinh viên chuyên ngành về Công nghệ thông tin.
            Đây là một môn học nền tảng, cho ta những khái niệm sơ khai về lập trình, các kiến thức chung nhất của một ngôn ngữ lập trình và đặc biệt là cho ta kĩ năng tư duy, giải quyết vấn đề trong lập trình nói chung.
            Môn học này thường sẽ được học ngay từ năm nhất đại học, và thông thường các trường sẽ lấy ngôn ngữ C/C++ để giảng dạy (có một số trường lựa chọn ngôn ngữ lập trình khác C#, Java, Python,...''',
            'cout': '''Cout là một đối tượng thuộc class ostream (kiến thức OOP) trong C++. Nó thường được sử dụng để hiển thị kết quả lên các thiết bị đầu ra của máy tính như màn hình, speaker,...(mình thường tiếp xúc với việc in kết quả lên màn hình).''',
            'cin': '''Cin là một đối tượng thuộc class istream (kiến thức OOP) trong C++. Nó thường sử dụng để nhận các giá trị đầu vào từ các thiết bị đầu vào của máy tính như bàn phím, micro,...'''
        }

        # Dict for answer why
        all_answers_why = {
            'comment': '''Trong bất cứ ngành nghề nào, chắc chắn bạn không chỉ làm việc một mình, đặc biệt trong lập trình, bạn muốn đồng nghiệp hoặc những thế hệ sau có thể dễ dàng hiểu được và kế thừa những dòng code của bạn viết ra, hoặc để vài năm sau đọc lại bạn vẫn đảm bảo hiểu được mình viết gì trong đó. Để làm được chuyện đó, ngoài việc tuân thủ các coding convention, naming convention, ... thì một trong những cách truyền đạt ý nghĩa đoạn code của bạn cho mọi người đó chính là COMMENT.''',
            'cplusplus': '''
            - Vai trò đặc biệt quan trọng của bộ đôi 2 ngôn ngữ lập trình C và C++ là phục vụ cho học lập trình cơ bản. Hầu hết các trường đào tạo công nghệ thông tin ở Việt Nam đều dùng 2 ngôn ngữ này làm môn cơ sở ngành. 
            - Môn lập trình C giúp bạn có nền tảng với kỹ thuật lập trình, các kiến thức cơ bản và tư duy lập trình. Môn lập trình C++ cung cấp kiến thức về lập trình hướng đối tượng. Cả 2 ngôn ngữ này cũng được sử dụng để học các môn học về cấu trúc dữ liệu và giải thuật.
            - Nếu bạn có kiến thức tốt về 2 ngôn ngữ này, thêm với kiến thức về cấu trúc dữ liệu và giải thuật. Việc học các kiến thức lập trình mới của bạn sẽ trở nên đơn giản hơn rất nhiều. Kiến thức mới ở đây có thể là công nghệ mới, ngôn ngữ lập trình mới,…
            - Ưu điểm vượt trội của C/C++ là tốc độ xử lý, hiệu năng cao. Do đó, nó thường được sử dụng trong các hệ thống lớn. Nơi mà hiệu năng, tốc độ là yếu tố then chốt của sản phẩm.
             ''',
            'include': 'Để có thể sử dụng một số hàm built-in cần thiết ta cần phải khai báo thư viện chứa các hàm đó để chương trình có thể thực thi.',
            'library': 'Một số thư viện cung cấp sẵn các hàm, các chức năng có sẵn để giúp chúng ta tiết kiệm thời gian coding hơn.',
            'namespace': 'Namespace được thiết kế để rút bớt thời gian khai báo các lệnh trong thư viện std. Các lệnh cout, cin và rất nhiều thứ khác được định nghĩa trong đó chính vì vậy bạn cũng có thể gọi các hàm này bằng cách sử dụng std :: cout, std :: cin, v.v.\n Chính vì vậy namespace được sinh ra để rút gọn thời gian khai báo các đầu chuẩn thư viện cho lập trình viên.',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': "Để lưu trữ một dữ liệu, bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.",
            'unsigned': '''Định nghĩa kiểu dữ liệu chỉ cho phép ta chứa các số nguyên không âm.''',
            'signed': '''Định nghĩa kiểu dữ liệu chỉ cho phép ta chứa các giá trị âm hoặc dương!''',
            'short': '''Điểm khác biệt của short so với int nằm ở việc có miền giá trị nhỏ hơn!''',
            'long': 'Điểm khác biệt của long so với int nằm ở việc có miền giá trị to hơn!',
            'type-modififer': 'Làm thay đổi các tính chất mặc định của chúng như miền giá trị,... Trong C++ gồm có 4 modifers đó là: unsigned, signed, short và long.',
            'constant': 'Constant hay const (Tạm dịch: Hằng số) trong C++ là một từ khóa dùng để chỉ định một biến hay một đối tượng (trong OOP) là một hằng - tức không thể làm thay đổi giá trị của nó kể từ sau khi khai báo từ khóa const.',
            'macro': 'Dùng để đặt lại tên của một chức năng, khối lệnh, giá trị,... theo ý của mình. Mình cũng có ví dụ như sau, giả sử mình muốn định nghĩa giá trị 3.14 có tên gọi là PI, mình có thể sử dụng macro như sau: #define PI 3.14',
            'wchar-t': 'Wide character khá giống với kiểu char ngoại trừ việc nó chiếm gấp đôi bộ nhớ và có thể một giá trị lớn hơn kiểu char (> 256)',
            'array': 'Cấu trúc dữ liệu Mảng sẽ giúp bạn lưu trữ danh sách các phần tử. Mình ví dụ như bạn sẽ cần lưu danh sách các sinh viên. Danh sách này sẽ được tổ chức sao cho bạn có thể truy xuất ngẫu nhiên nhanh chóng đến từng phần tử con. Chẳng hạn bạn muốn lấy thông tin sinh viên ở vị trí thứ 10.\n Pùm! Có ngay!.\n Danh sách này có thể được sắp xếp lại trật tự theo một tiêu chí nào đó, do đó bạn có thể nhanh chóng đọc ra top 10 sinh viên có điểm số cao nhất.\n Hay một lợi thế nữa của Mảng đó là với việc tổ chức các phần tử có kiểu dữ liệu tương tự nhau như vậy sẽ làm cho code của chúng ta tường minh và dễ quản lý hơn, giúp tối ưu code.',
            'structure': 'Kiểu dữ liệu structure được tạo thành từ một hoặc một nhóm kiểu dữ liệu xây dựng sẵn để tạo ra một tập hợp các biến thuộc cùng nhóm, những biến cùng nhóm này dùng để lưu trữ các dữ liệu có liên quan với nhau trong kiểu dữ liệu mới.\nCác bạn có thể tham khảo thêm tại : https://cpp.daynhauhoc.com/9/1-structs/',
            'class': 'Bạn tạo ra 1 class với những thuộc tính (property) và hành vi (method) của nó. Một object được tạo từ 1 class sẽ mang những đặc tính của class đó (với những thuộc tính, hành vi và quan hệ với các đối tượng khác được định nghĩa trong class).Class thường được xem như bộ khung (prototype) của object. Mình thì hiểu nó như 1 công cụ để nhóm các object ta sẽ tạo ra, ràng buộc các object đó phải có 1 số đặc tính nào đó. Mọi object tạo thành từ 1 class thì có những đặc tính giống nhau, đó là ý nghĩa của class.',
            'union': 'Dùng để gom nhóm các biến lại với nhau để từ đó hình thành một kiểu dữ liệu mới.',
            'pointer': 'Khi bạn muốn sử dụng một biến thì bạn phải cấp phát cho nó một bộ nhớ nhất định để có thể hoạt động.\nVí dụ như bạn tạo một mảng mà không cho biết số phần tử(tức là máy tính sẽ không biết cấp phát bao nhiêu ô nhớ) thì mảng đó không hợp lệ - sysnax error.\nĐể làm được điều đó thì ta dùng con trỏ để cấp phát động.',
            'enumeration': 'Enumeration hay enum (Tạm dịch: Kiểu liệt kê) là một kiểu dữ liệu trong C++ dùng để định nghĩa một tập các hằng số cố định,',
            'floating-point': 'Kiểu dấu chấm động cho phép ta lưu trữ cả phần thập phân của một số.',
            'double': 'Điểm khác biệt của double so với float nằm ở việc có miền giá trị lớn hơn.',
            'character': 'Kiểu char còn đặc biệt ở chỗ, nó vừa là kiểu kí tự nhưng cũng vừa là kiểu số nguyên (integer), chính vì thế ta cũng thể sử dụng số để đại diện cho các kí tự theo bảng mã ASCII khi làm việc với kiểu char.\nCú pháp: char <variable_name>;',
            'string': 'Kiểu string không phải là một kiểu dữ liệu được dựng sẵn trong C++ mà nó được cài đặt trong thư viện STL, vì vậy để sử dụng được string trước tiên các bạn cần phải khai báo: #include <string> cái đã nha!\nCú pháp: std::string <variable_name>;',
            'local-variable': 'Là biến được định nghĩa bên trong một khối lệnh. ',
            'global-variable': 'Chính vì được khai báo ngay đầu tập tin mà không nằm trong phạm vi của một khối lệnh nào nên biến toàn cục - đúng với tên gọi của nó sẽ có phạm vi hoạt động là toàn bộ tập tin code, tức là ta có thể sử dụng nó ở bất kì đâu mà ta muốn.',
            'auto': 'Ví dụ nếu ta khai báo: auto aStr = 10; thì kiểu dữ liệu của aStr lúc này sẽ là kiểu int',
            'static': 'Với biến static, dù đặt bên trong hay bên ngoài khối lệnh thì nó vẫn sẽ có hiệu lực - tức bất kì sự thay đổi giá trị ở đâu cũng làm biến static cập nhật đúng với giá trị đó - giống với Biến toàn cục (Global variable).',
            'vector': 'Khá giống với kiểu Mảng về chức năng, nhưng bên cạnh đó Vector còn cho thấy thêm một số điểm ưu việt hơn so với Array như việc không cần phải khai báo kích thước vì Vector có thể tự động tăng kích thước của nó lên, có thể biết được số lượng phần tử đang lưu bên trong nó hay có thể dùng được số phần tử âm,...',
            # Câu trả lời về các toán tử
            'comma-operator': '''Sử dụng dấu phẩy để khai báo đồng thời nhiêu biến khác nhau. Tiết kiệm được thời gian và làm code của bạn dễ nhìn và dễ đọc hơn.''',
            'ternary-operator': 'Một dạng rút gọn của if else tuy nhiên sẽ có kết quả trả về là False hoặc True.',
            'binary-operator': ' Có 5 toán tử số học 2 ngôi trong C++ đó là: Cộng (Addition : +), Trừ (Subtraction : -), Nhân (Multiplication : *), Chia lấy nguyên (Division : /), Chia lấy dư (Modulus : %)',
            'unary-operator': 'Ví dụ như việc bạn sử dụng dấu - để biểu diễn số âm kiểu -11, -60,...',
            'shift-operator': 'Shift Operators gồm hai loại là Left Shift và Right Shift, Left Shift sẽ dời dịch chuyển trái các bit của toán hạng đầu tiên, toán hạng thứ hai quyết định số vị trí cần dịch chuyển, hay nói cách khác  việc chuyển trái một số nguyên “x” với một số nguyên “y” (x << y) tương đương với việc nhân x với 2 ^ y và ngược lại với Right Shift.',
            'bitwise-operator': '''Bitwise khá mạnh trong việc xử lý các bài toán phức tạp, đây là một công cụ rất được ưa thích của các bạn tham gia Competitive Programming''',
            'logical-operator': 'Biểu diễn các biểu thức True hoặc False',
            'operator': 'Sử dụng toán tử (Operators) để biểu diễn các phép toán cơ bản.',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': 'Dùng để kiểm tra một biểu thức kiểu luận lý nào đó là đúng hay sai, nếu đúng thì sẽ thực thi tập chỉ thị bên trong khối if, nếu điều kiện sai thì sẽ bỏ qua khối lệnh if đó.',
            'loop': 'Sử dụng một vòng lặp để thực hiện các thao tác lặp đi lặp lại nhiều lần theo một ngữ cảnh nhất định, giảm thời gian thực hiện và biểu hiện code cho người lập trình.',
            'control-flow': 'Sử dụng Control Flow trong lập trình giúp ta thực hiện một tập các chỉ thị, các lệnh hay các lời gọi hàm được thực thi khi chạy chương trình.',
            'jump-statement': 'Trong C++, ta có thể biểu diễn Lệnh nhảy bằng các lệnh gồm Lệnh break, Lệnh continue, Lệnh goto và Lệnh return để thực hiện việc nhảy theo yêu cầu của thuật toán.',
            'for': "Sử dụng vòng lặp for cho các trường hợp vòng lặp có điều kiện về đầu cuối và bước nhảy cụ thể.",
            'break': 'Dùng để kết thúc một vòng lặp ngay lập tức kể cả khi nó vẫn còn có thể tiếp tục lặp.',
            'continue': 'Sử dụng continue khi bạn muốn bỏ qua một lần lặp trong vòng lặp.',
            'goto': "Dùng goto để giúp ta nhảy đến những vị trí được đấu dánh trong chương trình, tuy nhiên hạn chế sử dụng goto trong các trường hợp vì có thể gây ra memory leak nếu làm việc với con trỏ.",
            # Câu trả lời về function
            'function': 'Function cho phép lập trình viên cấu trúc chương trình thành những phân đoạn khác nhau để thực hiện những công việc khác nhau. Ta có thể tái sử dụng hàm ở nhiều nơi trong đoạn code của mình.',
            'parameter': 'Parameter sẽ đại diện cho một giá trị mà hàm của bạn sẽ nhận được khi được gọi.',
            'argument': 'Mỗi argument sẽ tương ứng với một parameter khi khai báo.',
            'recursion': 'Đệ quy (Recursion) giúp ta giải quyết các vấn đề bằng cách chia nhỏ nó thành phần nhỏ hoặc những vấn đề lặp đi lặp lại nhiều lần.\nĐệ quy thể hiện cực kì tốt khi làm việc với những vấn đề lặp đi lặp lại nhiều lần những có hướng tiếp cận quá phức tạp ',
            'pass-by-value': 'Pass by value (Tạm dich: Truyền tham trị) có thể được hiểu là giá trị của biến sẽ không bị thay đổi khi ta truyền biến này vào một hàm mà trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'pass-by-reference': 'Pass by reference (Tạm dịch: Truyền tham chiếu) có thể được hiểu là giá trị của biến sẽ bị thay đổi khi ta truyền biến này vào một hàm trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'return': 'Giúp ta trả về một kiểu dữ liệu mong muốn trong một hàm',
            'const-reference': 'Hiệu quả của việc sử dụng tham chiếu hằng chỉ thể hiện rõ khi làm việc với các đối tượng struct/class. Bạn có thể tìm đọc tại đây: https://stackoverflow.com/questions/7420780/what-is-a-constant-reference-not-a-reference-to-a-constant/7432351',
            'default-value': 'Vì khi thực hiện lời gọi hàm mà không truyền vào đối số tương ứng, trình biên dịch sẽ sử dụng giá trị đã được gán sẵn cho tham số đó khi thực thi hàm.',
            'main-function': 'Mỗi khi chương trình biên dịch, nó sẽ chỉ thực thi các lệnh mà bạn khai báo trong hàm main, chính vì vậy, việc khai báo hàm main cực kỳ quan trọng',
            'built-in-function': 'Vì các hàm này ta có thể gọi nó trực tiếp mà không cần phải khai báo và định nghĩa chúng bởi vì chúng đã được viết sẵn trong các thư viện của C++ như thư viện stdio.h, iostream,... Ta có thể tiết kiệm được thời gian code bằng các hàm bulit-in có sẵn, thay vì bạn phải khởi tạo lại một hàm có chức năng là tìm số nhỏ nhất hoặc lớn nhất, bạn có thể sử dụng hàm built-in min_element trong thư viện vector để thực hiện, điều này sẽ giúp cho bạn tiết kiệm được thời gian cũng như rút gọn bớt code của bạn đi.',
            'return-type': 'Giả sử ta khai báo một hàm kiểu int thì khi thực hiện lời gọi hàm, hàm này chắc chắn sẽ trả về một giá trị int.',
            'inline-function': 'Việc sử dụng Inline function (Hàm nội tuyến) sẽ giúp ta:\n1. Tiết kiệm chi phí gọi hàm.\n2. Tiết kiệm chi phí của các biến trên ngăn xếp khi hàm được gọi.\n3. Tiết kiệm chi phí cuộc gọi trả về từ một hàm.\n4. Có thể đặt định nghĩa hàm nội tuyến (inline functions) trong file tiêu đề (*.h) (nghĩa là nó có thể được include trong nhiều đơn vị biên dịch, hàm thông thường sẽ gây ra lỗi).',
            'lambda':'Lợi ích của lambda là không nhất thiết phải khai báo tên hàm ở 1 nơi khác, mà có thể tạo ngay 1 hàm (dùng 1 lần hay hiểu chính xác hơn là chỉ có 1 chỗ gọi 1 số tác vụ nhỏ). Như vậy sẽ giảm được thời gian khai báo 1 hàm.',
            'flowchart': '''Việc sử dụng lưu đồ thuật toán (flowchart) sẽ giúp ta tổ chức chương trình một cách hiệu quả hơn, diễn đạt thuật toán một cách lưu loát, dễ hiểu hơn,...''',
            'introduction-to-programming':'''Việc học môn Nhập môn lập trình sẽ cho bạn có những kiến thức nền tảng về lập trình như: Các kĩ năng tư duy, giải quyết vấn đề trong lập trình, các lý thuyết chung nhất mà bất kể mọi ngôn ngữ lập trình nào cũng có,...''',
            'cout':''' ''',
            'cin':''' '''
        }

        all_answers_how = {
            'comment': '''Để sử dụng Comment trong C++, các bạn có thể sử cú pháp // cho comment 1 dòng hoặc /* */ cho comment nhiều dòng. Ví dụ:
            int main(){
            // Đây là comment 1 dòng
            // Đây vẫn là comment 1 dòng
            /*
            Còn đây là
            Comment
            Nhiều dòng đóo
            Ahihi
            */
            return 0;
            }
             ''',
            'cplusplus': '''Để sử dụng C++, các bạn cần 2 thứ:
            Thứ nhất đó là một chiếc Text Editor với giao diện dễ nhìn như Notepad, VS Code, Sublime Text 3,...
            Thứ hai là một chiếc Compiler (trình biên dịch) như MinGW,...
            Còn không thì các bạn có thể tải các IDE về như Code::Blocks, Visual Studio, Eclipse, NetBeans,... để xài cho tiện nha
            Còn mà lười tải về mấy mớ ở trên thì lên Google gõ C++ compiler online để code ngay trên web luôn ha :3
            ''',
            'include': '''Để sử dụng cú pháp include, các bạn cần tìm cho mình một cái tên thư viện trong C++ phù hợp, sau đó thực hiện cú pháp như sau:
            #include <tên_thư_viện>
            Ví dụ:
            #include <iostream>
            #include <stdio.h>
            ''',
            'library': '''Để sử dụng các thư viện trong C++, ta chỉ cần sử dụng cú pháp #include <tên_library> là oke.Ví dụ:
            #include <iostream>  // Khai báo thư viện iostream
            #include <stdio.h> // Khai báo thư viện stdio.h
            ''',
            'namespace': '''Để sử dụng namespace ta sẽ khai báo như sau:
            namespace <tên_namespace>
            {
                int x, y; // Biến x y được khai báo
                          // bên trong tầm vực của namespace
            }
            Một số lưu ý với namespace:
            _ Chỉ được khai báo namespace ở tầm vực toàn cục (Global Scope)
            _ Có thể khai báo một namespace mới bên trong một namespace
            _ Có thể khai báo namespace cùng tên nhiều lần, các namespace có cùng tên sẽ được gom chung nội dung lại với nhau
             ''',
            'pseudo-code': '''Để sử dụng mã giả thì... các bạn chuẩn bị cho mình một tờ giấy, một cây bút, một thuật toán bất kì. Sau khi đã có đầy đủ những thứ trên, các bạn hãy diễn giải thuật toán đó dễ hiểu nhất có thể, không nhất thiết phải viết theo chuẩn ngôn ngữ lập trình nào.''',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': '''Để sử dụng được Variables, ta sẽ thực hiện cú pháp như sau: <kiểu_dữ_liệu> <tên_variable>;
            Ví dụ:
            int x = 5;
            float y;
            double a = 2.1;
            char b = 'c' ''',
            'unsigned': '''Sử dụng unsigned cũng giống như sử dụng biến vậy ấy.
             Ví dụ:
             unsigned x = 5;
             unsigned int y = 2;''',
            'signed': '''Sử dụng signed cũng giống như sử dụng biến ấy.
             Ví dụ:
             signed x = 5;
             signed int y = 2;''',
            'short': '''Để sử dụng short, ta thực hiện cú pháp: short <tên_variable>;''',
            'long': '''Để sử dụng long, ta thực hiện cú pháp: long <tên_variable>;''',
            'type-modififer': '''Để sử dụng type modifiers trong C++, các bạn có thể dùng các từ khóa short, long, signed hoặc unsigned.
            Ví dụ:
            short x = 2;
            long double = 10.10;
            unsigned char z;''',
            'typedef': '''Để sử dụng typedef, các bạn thực hiện cú pháp như sau: typedef <KDL> <tên_mới_của_KDL>
            Ví dụ:
            typedef int t
            typedef long l''',
            'constant': '''Để sử dụng từ khóa constant thì, mỗi khi khai báo một biến, các bạn chỉ cần thêm từ const trước kiểu dữ liệu là ok.
            Ví dụ:
            const int x = 5;
            const float y = 5.5;''',
            'macro': '''Để định nghĩa một macro, các bạn sẽ sử dụng từ khóa #define. Với cú pháp: #define <tên_macro> <biểu_thức>
            Ví dụ:
            #define PI 3.14
            #define ll long long
            #define sum(a,b) a + b''',
            'wchar-t': '''Để sử dụng wchar-t, ta thực hiện cú pháp: wchar-t <tên_variable>;''',
            'boolean':'''Để sử dụng kiểu boolean, ta thực hiện cú pháp: bool <tên_variable>;''',
            'data-type': '''Tùy thuộc vào kiểu dữ liệu các bạn muốn dùng mà ta sẽ sử dụng các từ khóa các nhau. Nếu cần một biến kiểu số nguyên, ta xài từ khóa int...''',
            '2d-array': '''Để sử dụng Mảng hai chiều, ta thực hiện cú pháp: <kiểu_dữ_liệu> <tên_variable>[<row_size>][<column_size>];''',
            'array': '''Để sử dụng Mảng một chiều, ta thực hiện cú pháp: <kiểu_dữ_liệu> <tên_variable>[<size>];''',
            'structure': '''Để sử dụng struct, ta thực hiện cú pháp:
            struct <tên_struct>{
                // khai báo các biến
            }
            Ví dụ:
            struct HinhChuNhat{
                int dai, rong;
            }''',
            'class': '''Để sử dụng class, ta thực hiện cú pháp sau:
            class <tên_class>{
                <phạm_vi_truy_cập>:
                // một vài thuộc tính
                // một vài phương thức
            };''',
            'union': ''' ''',
            'pointer': '''Để sử dụng con trỏ, ta thực hiện cú pháp: <kiểu_dữ_liệu> *<tên_variable>;''',
            'enumeration': '''Để sử dụng enum, ta thực hiện cú pháp:
            enum <tên_enum>{
                // Khai báo các biến, ngăn cách nhau bởi dấu phẩy
            }
            Ví dụ:
            enum DAY_OF_WEEK{
                CHUNHAT,
                THUHAI,
                THUBA,
                THUTU,
                THUNAM,
                THUSAU,
                THUBAY
            };''',
            'integer': '''Để sử dụng kiểu số nguyên (integer), ta thực hiện cú pháp: int <tên_variable>;''',
            'floating-point': '''Để sử dụng kiểu dấu chấm động (floating point), ta thực hiện cú pháp: float <tên_variable>;''',
            'double': '''Để sử dụng kiểu double, ta thực hiện cú pháp: double <tên_variable>; ''',
            'character': '''Để sử dụng kiểu character, ta thực hiện cú pháp: char <tên_variable>; ''',
            'string': '''Để sử dụng kiểu string, trước hết ta cần khai báo thư viện string bằng cách sử dụng cú pháp: #include <string.h>
            Sau đó để khai báo một biến kiểu string ta thực hiện cú pháp: string <tên_variable>; ''',
            'local-variable': '''Biến cục bộ chỉ là một khái niệm hàn lâm, không có cách thực hiện chung chung cụ thể''',
            'auto': '''Để sử dụng kiểu auto, ta thực hiện cú pháp: auto <tên_variable>;
            Lưu ý: Chỉ có thể sử dụng kiểu auto ở phiên bản C++ 11 trở lên thôi đó nha''',
            'external': ''' ''',
            'static': '''Để sử dụng biến tĩnh (static), ta sẽ khai báo từ khóa static trước kiểu dữ liệu của biến, có thể sử dụng biến tĩnh trong hàm hoặc trong class. Ví dụ:
            int foo(){
                static int count = 0; // giá trị của count sẽ được khai báo một lần sau lời gọi hàm đầu tiên và tồn tại trong suốt thời gian thực thi chương trình
                cout << ++count << " ";
            }''',
            'vector': '''Để có thể sử dụng vector, trước tiên ta cần phải khai báo thư viện vector với cú pháp: #include <vector>
            Sau đó, ta sẽ khai báo một vector với cú pháp như sau: std::vector <data_type>variable_name;''',
            'reference-variable': '''Để sử dụng một biến tham chiếu, ta sẽ dùng cú pháp sau: data_type &variable_name = declared_variable''',
            # Câu trả lời về các toán tử
            'decrement-operator': '''Để sử dụng toán tử giảm, ta sử dụng cú pháp như sau: variable-- hoặc --variable.''',
            'increment-operator': '''Để sử dụng toán tử tăng, ta sử dụng cú pháp như sau: variable++ hoặc ++variable.''',
            'dereference-operator': '''Để sử dụng toán tử trỏ, ta sẽ sử dụng cú pháp như sau: data_type variable_name = *declared_variable;''',
            'address_of-operator': '''Để sử dụng toán tử địa chỉ, ta sẽ sử dụng cú pháp sau: &declared_variable, cú pháp này sẽ trả về cho ta 1 giá trị.''',
            'comma-operator': '''Toán tử phẩy có rất nhiều công dụng, ta có thể sử dụng nó để khai báo nhiều biến có cùng kiểu dữ liệu như int a, b, c; Hoặc ta dùng nó để truyền các đối số vào trong lời gọi hàm.''',
            'ternary-operator': '''Để sử dụng toán tử ba ngôi, ta sẽ sử dụng cú pháp như sau: (expression) ? value_if_true : value_if_false. Cú pháp này sẽ trả về cho ta một giá trị cụ thể.''',
            'binary-operator': '''Để sử dụng toán tử hai ngôi, ta có thể thực hiện theo cú pháp: variable_1 phép_toán variable_2.
            Ví dụ:
            1 + 2
            5 * 2
            10 % 2''',
            'unary-operator': '''Để sử dụng toán tử hai ngôi, ta có thể sử dụng các toán tử tăng/giảm, toán tử trỏ, toán tử địa chỉ,...''',
            'shift-operator': '''Để sử dụng toán tử dời bit, ta có thể sử dụng các ký hiệu như << (left shift), >> (right shift).''',
            'bitwise-operator': '''Để sử dụng toán tử bit, ta có thể sử dụng các ký hiệu như & (AND), | (OR), ^ (XOR), ~ (NOT),...''',
            'logical-operator': '''Để sử dụng toán tử logic, ta có thể sử dụng các ký hiệu như && (and), || (or) hoặc ! (not). Toán tử này rất thường được sử dụng khi khai báo điều kiện cho if.Ví dụ: (x == y) && (z != 3)''',
            'comparison-operator': '''Để sử dụng toán tử so sánh, ta có thể sử dụng các ký hiệu so sánh như ==, !=, >=, <=,...Ví dụ: x != y, 2 == 2,...''',
            'arithmetic-operator': '''Để sử dụng toán tử số học, ta có thể sử dụng các ký hiệu +, -, *, /, % để biểu diễn. Ví dụ: x + y, 5 / 2,...''',
            'assignment-operator': '''Để sử dụng toán tử gán, ta sẽ sử dụng cú pháp: variable_1 = variable_2''',
            'operator': '''Để sử dụng toán tử, thứ đầu tiên ta cần là các toán hạng (biến), thứ hai là một phép toán cụ thể như +, -, *, /, %, =, ==,...Việc thứ ba là ghép hai thứ đó vào nhau, sau khi biên dịch nó sẽ trả về cho ta một giá trị.''',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': '''Để dùng lệnh if, bạn sử dụng cú pháp sau:
            if(<boolean_expression>){
                //some codes here...
            }''',
            'loop': '''Để dùng lệnh lặp trong C++, bạn có thể sử dụng các lệnh như for, while, do while...''',
            'control-flow': '''Để dùng các lệnh điều khiển trong C++, bạn có thể sử dụng các lệnh if, for, while, switch,...''',
            'selection-statement': '''Để dùng các lệnh lựa chọn, các bạn có thể sử dụng các lệnh if, switch.''',
            'iteration-statement': '''Để dùng lệnh lặp trong C++, bạn có thể sử dụng các lệnh như for, while, do while...''',
            'jump-statement': '''Để sử dụng các lệnh nhảy, bạn có thể sử dụng các cú pháp break, continue, goto.''',
            'for': '''Để sử dụng vòng lặp for, bạn sử dụng cú pháp như sau:
            for(<khai_báo_biến_lặp>;<điều_kiện_dừng>;<cập_nhật_giá_trị>){
                //Some codes here...
             }\n''',
            'while': '''Để sử dụng vòng lặp while, bạn sử dụng cú pháp như sau:
            while(<biểu_thức_điều_kiện>)
            {
                //some codes here...
            }''',
            'do-while': '''Để sử dụng vòng lặp do while, bạn sử dụng cú pháp như sau:
            do {
                // Some codes here;
            } while (<biểu_thức_điều_kiện>);''',
            'switch': '''Để sử dụng lệnh switch, bạn sử dụng cú pháp như sau:
            switch (n) // n là biến kiểu số nguyên
            {
                case 1: // Sẽ thực thi khối lệnh ở đây nếu n == 1;
                        break;
                case 2: // Sẽ thực thi khối lệnh ở đây nếu n == 2;
                        break;
                default: // Nếu n không bằng với bất kì case nào thì sẽ thực thi khối lệnh ở đây;
            }''',
            'break': '''Để sử dụng từ khóa break, bạn chỉ việc đặt nó trong một vòng lặp bất kì, hoặc khi sử dụng lệnh switch. Ví dụ:
            for(int i = 0; i < n; ++i){
                if(i % 2 == 0){
                    break; // Khi i là số chẵn thì ngắt vòng lặp
                }
            }''',
            'continue': '''Để sử dụng từ khóa continue, bạn chỉ việc đặt nó trong một vòng lặp bất kì, bạn sẽ thấy rõ công dụng của nó. Ví dụ:
            for(int i = 0; i < n; ++i){
                if(i % 2 == 0){
                    continue; // Khi i là số chẵn thì chuyển tới lần lặp tiếp theo
                }
                if(i % 2 != 0)
                    cout << "Hí ae..." << endl;
                }
            }''',
            'goto': '''Để sử dụng goto, bạn sẽ dùng cú pháp như sau:
            goto label;
            .
            .
            .
            label: statements''',
            'if-else': '''Để sử dụng if else, bạn dùng cú pháp như sau:
            if(<điều_kiện>){
                // Some codes here...
            }
            else{
                // Some codes here...
            }''',
            'if-else-if-ladder': '''Để sử dụng if else if Ladder (cầu thang if else), bạn dùng cú pháp như sau:
            if(<điều_kiện_1>){
                // Some codes here...
            }
            else if(<điều_kiện_2>){
                // Some codes here...
            }
            else if(<điều_kiện_3>){
                // Some codes here...
            }
            ...
            Bạn có thể thỏa thích đặt bao nhiêu cái else if đan xen với nhau như vậy cũng được nha.
            Lưu ý là khi một biểu thức điều kiện nào thỏa mãn, thì tất cả các biểu thức về sau sẽ không được trình biên dịch duyệt qua.''',
            'nested-if': '''Để sử dụng if lồng if, bạn dùng cú pháp như sau:
            if(<điều_kiện_1>){
                if(<điều_kiện_2>){
                    // Some code heres...
                }
            }
            ''',
            # Câu trả lời về function
            'function': '''Để sử dụng hàm, bạn dùng cú pháp như sau:
            <kiểu_trả_về_của_hàm> <tên_hàm>(<các_tham_số>){
                // Some code heres...
                return <value>; // Dòng này không bắt buộc khi kiểu trả về của hàm là void
            }''',
            'parameter': '''Để sử dụng tham số, các bạn hãy khai báo nó khi thực hiện khai báo hàm. Ví dụ:
            int sum(int a, int b){ // a và b là tham số
                return a + b;
            }''',
            'argument': '''Để sử dụng đối số, các bạn đơn giản chỉ việc...truyền bất cứ giá trị gì vào hàm khi thực hiện lời gọi hàm thôi. Ví dụ:
            int answers = sum(a, b); // a, b là đối số''',
            'recursion': '''Để sử dụng đệ quy, các bạn cần phải tìm ra được phương trình chung cho bài toán và điều kiện dừng của nó và diễn giải chúng ở trong hàm. Ví dụ:
            int sum(int n){
                if(n == 1){
                    return 1;
                }
                return n + sum(n - 1);
            }''',
            'pass-by-value': '''Để thực hiện truyền tham trị, các bạn sẽ làm việc khai báo tham trị khi khai báo hàm. Ví dụ:
            int sum(int a, int b){ // a và b là tham trị
                return a + b;
            }''',
            'pass-by-reference': '''Để thực hiện truyền tham chiếu, các bạn cần thêm dấu & ở trước tên tham số khi thực hiện khai báo hàm. Ví dụ:
            int swap(int &a, int &b){ // a và b là tham chiếu
                int temp = a;
                a = b;
                b = temp;
            }''',
            'return': '''Để sử dụng từ khóa return, các bạn hãy đặt nó khi viết hàm. Ví dụ:
            int sum(int a, int b){ 
                return a + b; // khi thực hiện lời gọi hàm này thì sẽ trả về giá trị a + b
            } 
            ''',
            'return-type': '''Để thực hiện khai báo kiểu trả về của hàm, các bạn sẽ khai báo nó chung với việc khai báo hàm.Ví dụ:
            int sum(int a, int b){ // kiểu trả về của hàm này là kiểu int
                return a + b;
            }''',
            'const-reference': '''Để sử dụng tham chiếu hằng, các bạn sẽ sử dụng cú pháp sau:
            int sum(const int &a, const int &b){ // a và b là tham chiếu hằng
                return a + b;
            }''',
            'inline-function': '''Để sử dụng hàm nội tuyến, các bạn đặt từ khóa inline ngay trước kiểu trả về của hàm. Ví dụ:
            inline int sum(int a, int b)
            {
                return a + b;
            }
            Lưu ý là hàm nội tuyến sẽ không thực hiện được khi bên trong hàm chứa vòng lặp, biến tĩnh, đệ quy hay lệnh switch, goto.''',
            'default-value': '''Để sử dụng tham số mặc nhiên, các bạn sẽ gán tham số của hàm bởi một giá trị nào đó, khi đó cho dù lúc bạn thực hiện lời gọi hàm, bạn không truyền bất kì đối số nào cho tham số đó thì tham số đó sẽ lấy giá trị mà bạn đã gán lúc khai báo hàm. Ví dụ:
            int sum(int a=0, int b=0){ // giá trị mặc định của a và b là 0
                return a + b; 
            }
            
            int main(){
                cout << sum() << endl; // Sẽ in ra giá trị 0
                return 0;   
            }''',
            'main-function': '''Để sử dung hàm main...hình như mỗi lần tạo project mới là nó đã viết sẵn cho bạn rồi đó :)), nên nhớ là hàm main chỉ có một thôi nha bạn.''',
            'built-in-function': '''Để sử dụng các hàm dựng sẵn, các bạn hãy tìm hiểu xem hàm đó được dựng trong thư việc nào và nằm trong namespace nào (nếu có). Giả mình muốn dùng hàm căn bậc 2 sqrt(), mình tìm hiểu và biết rằng nó được dựng trong thư viện math.h, sau đó mình sẽ làm như sau:
            #include <iostream>
            #include <math.h>
            
            int main()
            {
                cout << sqrt(4) << endl; // Sẽ in ra màn hình số 2
                return 0;
            }''',
            'lambda': '''Để sử dụng hàm lambda, có 4 cú pháp như sau:
            [ capture-list ] ( params ) mutable(optional) exception attribute -> ret { body }  
            [ capture-list ] ( params ) -> ret { body }    
            [ capture-list ] ( params ) { body }    
            [ capture-list ] { body }
            Trong đó:
            capture-list: là danh sách các biến có thể được truy cập ngoài scope của hàm lambda, với dấu = là capture by value (giống truyền tham trị) và dấu 7 là capture by reference(giống truyền tham chiếu)
            params: là nơi khai báo các tham số, giống khai báo ở hàm thông thường.
            mutable: là từ khóa giúp ta có thể thay đổi giá trị của biến được capture by value trong hàm lambda nhưng vẫn không bị thay đổi giá trị khi ra ngoài hàm này.
            body: là nội dung code bên trong hàm lambda.
            -> ret: là cách diễn đạt hàm lambda sẽ trả về một giá trị nào đó.
            ''',
            'flowchart':'''Để vẽ lưu đồ thuật toán (flowchart), bạn chỉ cần một cây bút, một quyển tập và một bài toán/thuật toán bất kì để bắt đầu thực hiện vẽ lưu đồ thuật toán với bài toán bạn chọn. Một số ký hiệu bạn phải sử dụng:
            _ Hình oval: Bắt đầu/Kết thúc chương trình
            _ Hình thoi: Điều kiện rẽ nhánh
            _ Dấu mũi tên: Luồng xử lý
            _ Hình bình hành: Nhập/Xuất
            _ Hình chữ nhật: Xử lý/Tính toán/Gán
            _ Hình mũi tên rẽ trái: Trả về (return)
            _ Hình tròn: Điểm kết nối''',
            'introduction-to-programming':'''Để có thể đạt điểm cao/qua môn với môn Nhập môn lập trình này, cần phải xác định trước với bản thân mình rằng môn học này khác biệt hoàn toàn so với các môn học khác ta từng được học, và nó là một cực kì quan trọng đối với các lập trình viên chúng ta bởi vì nó sẽ là nền móng vững chắc để có thể học tiếp các môn học về sau.
            Đặc biệt là với đặc thù của môn học này, ta luôn cần phải trau dồi kĩ năng qua việc làm các bài tập lớn/nhỏ ở trên lớp, đồng thời phải luôn cố gắng tìm tòi thêm trên internet về các kiến thức liên quan đến bài học chứ không nên chỉ bám vào giáo trình trên giảng đường đơn thuần.''',
            'cout':''' ''',
            'cin':''' '''
        }

        all_answers_example = {
            'comment': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                // Đây là comment
                /*
                Đây 
                cũng là 
                comment 
                nhưng được ghi nhiều dòng
                */
                return 0;
            }''',
            'cplusplus': '''Một chương trình C++ cơ bản trông như thế này nè:
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << "Hello world";
                return 0;
            }''',
            'include': '''
            #include <iostream> // include ở đây
            #include <stdio.h> // include ở đây
            #include <stdlib.h> // include ở đây
            #include <math.h> // include ở đây

            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'library': '''
            #include <iostream> // thư viện ở đây
            #include <stdio.h> // thư viện ở đây
            #include <stdlib.h> // thư viện ở đây
            #include <math.h> // thư viện ở đây

            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'namespace': '''
            #include <iostream>
            
            using namespace std; // Sử dụng namespace std

            namespace foo{ // Khai báo namespace tên foo
                void print_foo(){
                    cout << "Hello world" << endl;
                }
            }
            
            int main()
            {
                foo::print_foo(); // Gọi hàm từ namespace foo
                return 0;
            }''',
            'pseudo-code': '''Viết mã giả cho bài toán tìm số lớn nhất:
            Nhập a;
            Nhập b;
            If a > b then a lớn nhất
            else b lớn nhất''',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 1; // Đây là biến nè
                float b = 2.5; // Đây cũng là biến nè
                cout << a << " " << b << endl; // Thử in hai biến trên ra nè
                return 0;
            }''',
            'unsigned': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                unsigned int a = 2; // Đây là biến có modifier unsigned nè
                return 0;
            }''',
            'signed': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                singed int a = 2; // Đây là biến có modifier signed nè
                return 0;
            }''',
            'short': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                short a = 10; // Đây là biến có modifier short nè
                return 0;
            }''',
            'long': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                long x = 1000; // Đây là biến có modifier long nè
                return 0;
            }''',
            'type-modififer': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                // Đây là những modifiers
                unsigned x = 10; 
                signed y = 20;
                short z = 1; 
                long long k = 100000;
                return 0;
            }''',
            'typedef': '''
            #include <iostream>
            
            using namespace std;

            // Sử dụng typedef để đặt nickname cho hai kiểu dữ liệu sau đây
            typedef int SONGUYEN;
            typedef long long ll;
            
            int main()
            {
                // Có thể sử dụng nickname đã đặt để thay thế cách khai báo cũ
                SONGUYEN a = 2;
                ll b = 10;
                return 0;
            }''',
            'constant': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                const int a = 10; // Khai báo biến hằng
                return 0;
            }''',
            'macro': '''
            #include <iostream>
            // Khai báo các macros
            #define PI 3.14 
            #define MAX(a,b) (a > b) ? a : b            
            using namespace std;

            
            int main()
            {
                cout << PI << endl;
                cout << MAX(4,5) << endl;
                return 0;
            }''',
            'wchar-t': ''' ''',
            'boolean':'''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                bool a = true;
                if(a){
                    cout << "Hello boolean" << endl;
                }
                return 0;
            }
            ''',
            'data-type': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                // Đây là một số kiểu dữ liệu trong C++
                int a; // Kiểu số nguyên
                float b; // Kiểu dấu chấm động
                double c; // Vẫn là kiểu dấu chấm động nhưng có miền giá trị to hơn
                bool d; // Kiểu luận lý
                char e; // Kiểu kí tự
                return 0;
            }''',
            '2d-array': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a[100][100]; // Khai báo mảng hai chiều
                return 0;
            }''',
            'array': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a[100]; // Khai báo mảng một chiều
                return 0;
            }''',
            'structure': '''
            #include <iostream>
            
            using namespace std;

            struct HINHCHUNHAT{ // Đây là khai báo struct
                int chieudai, chieurong;
            };
            
            int main()
            {
                HINHCHUNHAT a;
                cout << "Nhap chieu dai va chieu rong cua hinh chu nhat: ";
                cin >> a.chieudai >> a.chieurong;
                return 0;
            }''',
            'class': '''
            #include <iostream>
            
            using namespace std;
            
            class HINHCHUNHAT{ // Đây là khai báo class
                private:
                    int chieudai, chieurong;
                public:
                    void Nhap(){
                        cout << "Nhap chieu dai va chieu rong: ";
                        cin >> chieudai >> chieurong ;
                    }
                    void Xuat(){
                        cout << "Chieu dai la: " << chieudai << endl ;
                        cout << "Chieu rong la: " << chieurong << endl;
                    }
            };
            
            int main()
            {
                HINHCHUNHAT a;
                a.Nhap();
                a.Xuat();
                return 0;
            }''',
            'union': '''
            #include <iostream>
            
            using namespace std;

            union HINHCHUNHAT{ // Đây là khai báo union
                int chieudai, chieurong;
            };
            
            int main()
            {
                HINHCHUNHAT a;
                cout << "Nhap chieu dai va chieu rong cua hinh chu nhat: ";
                cin >> a.chieudai >> a.chieurong;
                return 0;
            }''',
            'pointer': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int *a; // Đây là khai báo con trỏ kiểu số nguyên
                int b = 10;
                // Một số khả năng của con trỏ
                a = &b; // Con trỏ a đang giữ địa chỉ của biến b
                cout << *a << endl; // In ra 10, vì lúc này a đang tham chiếu đến b
                cout << (*a)++ << endl; // In ra 10
                cout << b << endl; << // In ra 11, vì a tham chiếu đến b nên mọi sự thay đổi ở a cũng sẽ ảnh hưởng đến b, nói cách khác a là một tên gọi khác của b
                return 0;
            }''',
            'enumeration': '''
            #include <iostream>
            
            using namespace std;

            enum DAY_OF_WEEK{
                CHUNHAT,
                THUHAI,
                THUBA,
                THUTU,
                THUNAM,
                THUSAU,
                THUBAY
            };
            
            int main()
            {
                cout << THUHAI << endl; // Thử in giá trị trong enum
                DAY_OF_WEEK w; // Enum như một kiểu dữ liệu thông thường
                return 0;
            }''',
            'integer': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10; // Đây là biến kiểu integer
                return 0;
            }''',
            'floating-point': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                float a = 1.1; // Đây là biến kiểu float
                return 0;
            }''',
            'double': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                double a = 10.10; // Đây là biến kiểu double
                return 0;
            }''',
            'character': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                char a = '2'; // Đây là biến kiểu kí tự
                return 0;
            }''',
            'string': '''
            #include <iostream>
            #include <string.h> // Phải khai báo thư viên string.h trước khi dùng string

            using namespace std;
            
            int main()
            {
                string a = "Hello World"; // Đây là biến kiểu string
                return 0;
            }''',
            'local-variable': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1){
                    int a = 2; // Đây là biến cục bộ, nó nằm trong tầm vực của khối if này
                    cout << a << endl;
                }
                return 0;
            }''',
            'auto': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                auto a = 2; // Đây là biến kiểu auto, chỉ dùng được ở C++ 11
                return 0;
            }''',
            'external': ''' ''',
            'static': '''
            #include <iostream>
            
            using namespace std;

            void foo(){
                static int count = 0; // Khởi tạo biến tĩnh
                cout << ++cout << " ";
            }
            
            int main()
            {
                for(int i = 0; i < 5; ++i){
                    foo(); // In ra 1 2 3 4 5
                }
                return 0;
            }''',
            'vector': '''
            #include <iostream>
            #include <vector>

            using namespace std;
            
            int main()
            {
                vector <int>v; // Khai báo vector kiểu int
                for(int i = 0; i < 10; ++i){
                    int input;
                    cout <<"Nhap phan tu thu " << i + 1 << " cua vector: ";
                    cin >> input;
                    v.push_back(input);
                }
                return 0;
            }''',
            'reference-variable': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10;
                int &b = a; // b là biến tham chiếu đến a
                return 0;
            }''',
            # Câu trả lời về các toán tử
            'decrement-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10;
                // Hai cách sử dụng toán tử giảm
                cout << a-- << endl; // In ra 10, nhưng khi kết thúc lệnh này thì a = 9
                cout << --a << endl; // In ra 8, kết quả phép trừ sẽ được hiển thị ngay tại dòng này luôn
                cout << a-- << " " << --a << endl; // In ra 7 6, trình biên dịch sẽ biên dịch từ bên phải sang trái
                return 0;
            }''',
            'increment-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'dereference-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10;
                // Hai cách sử dụng toán tử tăng
                cout << a++ << endl; // In ra 10, nhưng khi kết thúc lệnh này thì a = 11
                cout << ++a << endl; // In ra 12, kết quả phép cộng sẽ được hiển thị ngay tại dòng này luôn
                cout << a++ << " " << ++a << endl; // In ra 13 14, trình biên dịch sẽ biên dịch từ bên phải sang trái
                return 0;
            }''',
            'address_of-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10;
                cout << &a << endl; // In ra địa chỉ của biến a
                return 0;
            }''',
            'comma-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a, b, c; // Sử dụng toán tử phẩy để khai báo nhiều biến cùng lúc
                return 0;
            }''',
            'ternary-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << (2 > 1) ? 10 : 0; // In ra 10 vì 2 > 1 là đúng
                return 0;
            }''',
            'binary-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << 2 + 1 << endl; // Dùng toán tử hai ngôi để + 2 và 1
                return 0;
            }''',
            'unary-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 1;
                cout << ++a << endl; // Dùng toán tử một ngôi để tăng giá trị của a lên 1
                return 0;
            }''',
            'shift-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'bitwise-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'logical-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 2;
                if(a == 2 || a > 1) // Dùng toán tử logic để làm phong phú thêm điều kiện if
                {
                    cout << "HI..." << endl;
                }
                return 0;
            }''',
            'comparison-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 1;
                if(a == 1){ // Dùng toán tử so sánh để so sánh a với 1
                    cout << "Hi..." << endl;
                }
                return 0;
            }''',
            'arithmetic-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10;
                // Đây là tất cả các toán tử số học
                cout << 1 + 1 << endl;
                cout << a - 2 << endl;
                cout << a * 3 << endl;
                cout << a / a << endl;
                cout << 4 % 2 << endl;
                return 0;
            }''',
            'assignment-operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 10; // Dùng toán tử gán để gán a = 10
                int b = a; // Dùng toán tử gán để gán b = a
                return 0;
            }''',
            'operator': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << 2 + 2 << endl; // Dấu + là toán tử nè
                cout << 2 == 2 << endl; // Dấu == cũng là toán tử nè
                return 0;
            }''',
            'scope-resolution-operator':'''
            #include <iostream>

            // Không thấy using namespace std ở đâu ta
            
            int main()
            {
                // Dùng toán tử định phạm vi để sử dụng các hàm trong namespace std
                std::cout << "Hello world" << std::endl;
                return 0;
            }''',
            # Câu trả lời về control flow
            'if': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1 == 2){ // Khai báo if
                    cout << "Có dụ này nữa hả...???" << endl;
                }
                return 0;
            }''',
            'loop': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 1; i <= 5; ++i){ // Dùng vòng lặp để in 5 dòng hello world nè
                    cout << "Hello world" << endl;
                }
                return 0;
            }''',
            'control-flow': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1 == 2){ // Đây là một control flow
                    cout << "Có dụ này nữa hả...???" << endl;
                }
                int count = 0;
                while(1){ // Đây là một control flow
                    cout << "Hehe boiz..." << endl;
                    count++;
                    if(count == 5){
                        break; // Đây là một control flow
                    }
                }
                return 0;
            }''',
            'selection-statement': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1 == 2){ // Đây là một lệnh chọn
                    cout << "Có dụ này nữa hả...???" << endl;
                }
                int a = 2;
                switch(a){ // Đây cũng là một lệnh chọn
                    case 1: cout << "1" << endl;
                            break; 
                    case 2: cout << "2" << endl;
                            break; 
                }
                return 0;
            }''',
            'iteration-statement': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 0; i < 10; ++i){ // Đây là lệnh lặp
                    cout << "hehe boiz..." << endl;
                }
                return 0;
            }''',
            'jump-statement': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 0; i < 10; ++i){ 
                    cout << "hehe boiz..." << endl;
                    if(i == 7){
                        break; // Đây là lệnh nhảy
                    }
                }
                return 0;
            }''',
            'for': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 0; i < 10; ++i){ // Đây là lệnh for
                    cout << "hehe boiz..." << endl;
                }
                return 0;
            }''',
            'while': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int count = 0;
                while(count < 10){ // Đây là lệnh while
                    cout << "Hehe boiz..." << endl;
                    count++;
                }
                return 0;
            }''',
            'do-while': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int count = 0;
                do { // Đây là lệnh do while
                    cout << "Hehe boiz..." << endl;
                    count++;
                } while (count < 10);
                return 0;
            }''',
            'switch': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int n;
                cout << "Nhap n: ";
                cin >> n;
                switch(n){ // Đây là lệnh switch
                    case 1: cout << "1" << endl;
                            break;
                    case 2: cout << "2" << endl;
                            break;
                    default: cout << "..." << endl;
                }
                return 0;
            }''',
            'break': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 0; i < 10; ++i){ 
                    cout << "hehe boiz..." << endl;
                    if(i == 7){
                        break; // Đây là lệnh break
                    }
                }
                return 0;
            }''',
            'continue': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                for(int i = 0; i < 10; ++i){ 
                    if(i % 2 == 0){
                        continue; // Đây là lệnh continue
                    }
                    cout << "hehe boiz..." << endl;
                }
                return 0;
            }''',
            'goto': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'if-else': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1 == 2){ 
                    cout << "Có dụ này nữa hả...???" << endl;
                }
                else{ // Dùng else để biểu diễn các trường hợp còn lại
                    cout << "Có hộ tui cái !" << endl;
                }
                return 0;
            }''',
            'if-else-if-ladder': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                if(1 == 2){ 
                    cout << "Có dụ này nữa hả...???" << endl;
                }
                else if(1 == 3){ // Nếu if trên sai thì sẽ duyệt if này
                    cout << "Thiệt luôn hả trời...?!" << endl;
                }
                return 0;
            }''',
            'nested-if': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 2;
                if(a > 0){ 
                    if(a < 0){ // if được lồng bên trong if
                        cout << "Làm gì có vụ này..." << endl;
                    }
                }
                return 0;
            }''',
            # Câu trả lời về function
            'function': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a, int b) // Khai báo hàm
            {
                sum = a + b;
                return sum;
            }
            
            int main()
            {
                cout << sum(1,1) << endl; // Thực hiện lời gọi hàm
                return 0;
            }''',
            'parameter': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a, int b) // a và b là các tham số nè
            {
                sum = a + b;
                return sum;
            }
            
            int main()
            {
                cout << sum(1,1) << endl;
                return 0;
            }''',
            'argument': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a, int b) 
            {
                sum = a + b;
                return sum;
            }
            
            int main()
            {
                cout << sum(1,1) << endl; // hai số 1 ở đây là đối số nè
                return 0;
            }''',
            'recursion': '''
            #include <iostream>
            
            using namespace std;

            int sum(int n) // Hàm đệ quy
            {
                if(n == 1){ // Điều kiện dừng
                    return 1;
                }
                return n + sum(n - 1); // Gọi lại hàm này bên trong hàm này
            }
            
            int main()
            {
                cout << sum(5) << endl; // In ra 15
                return 0;
            }''',
            'pass-by-value': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a, int b) // a và b là tham trị
            {
                sum = a + b;
                return sum;
            }
            
            int main()
            {
                cout << sum(1,1) << endl;
                return 0;
            }''',
            'pass-by-reference': '''
            #include <iostream>
            
            using namespace std;

            void swap(int &a, int &b) // a và b là tham chiếu
            {
                int temp = a;
                a = b;
                b = temp;
            }
            
            int main()
            {
                int a = 1, b = 2;
                swap(a, b);
                cout << a << " " << b << endl; // a = 2, b = 1
                return 0;
            }''',
            'return': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a, int b) 
            {
                sum = a + b;
                return sum; // hàm này sẽ trả về giá trị của sum
            }

            void foo(int a)
            {
                if(a > 0){
                    return; // Hàm void vẫn có thể sử dụng return được, nhưng nó sẽ không trả về giá trị gì hết
                }
                cout << "foo" << endl;
            }
            
            int main()
            {
                cout << sum(1,1) << endl; 
                return 0;
            }''',
            'return-type': '''
            int foo_int(int a, int b) // Kiểu trả về int
            {
                return 0;
            }

            float foo_float(float a, float b) // Kiểu trả về float
            {
                return 0.0; 
            }

            void foo_void() // Kiểu trả về void
            {
                return;
            }
            ''',
            'const-reference': '''
            #include <iostream>
            
            using namespace std;

            int sum(const int &a, const int &b) // a và b là tham chiếu hằng
            {
                return a + b;
            }
            
            int main()
            {
                cout << sum(1,1) << endl;
                return 0;
            }''',
            'inline-function': '''
            #include <iostream>
            
            using namespace std;

            inline int sum(int a, int b) // Khai báo hàm nội tuyến
            {
                return a + b;
            }
            
            int main()
            {
                cout << sum(1,1) << endl;
                return 0;
            }''',
            'default-value': '''
            #include <iostream>
            
            using namespace std;

            int sum(int a = 0, int b = 0) // a và b có giá trị mặc định là 0
            {
                return a + b;
            }
            
            int main()
            {
                cout << sum() << endl; // In ra 0 dù mình không truyền bất kì đối số nào
                return 0;
            }''',
            'main-function': '''
            #include <iostream>
            
            using namespace std;
            
            int main() // Đây là hàm main
            {
                cout << "Hello world" << endl;
                return 0;
            }''',
            'built-in-function': '''
            #include <iostream>
            #include <math.h>

            using namespace std;
            
            int main()
            {
                cout << sqrt(4) << endl; // Dùng hàm căn bậc 2 đã được dựng sẵn trong thư viện math.h
                return 0;
            }''',
            'lambda': '''
            #include <iostream>
            
            using namespace std;
            
            int main()
            {
                int a = 2, b = 3;
                [=](){int sum = a + b; cout << sum << endl;}(); // Đây là hàm lambda
                return 0;
            }''',
            'flowchart':''' ''',
            'introduction-to-programming':''' ''',
            'cout':''' ''',
            'cin':''' '''
        }

        all_answers_when = {
            'comment': ''' ''',
            'cplusplus': ''' ''',
            'include': ''' ''',
            'library': ''' ''',
            'namespace': ''' ''',
            'pseudo-code': ''' ''',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': ''' ''',
            'unsigned': ''' ''',
            'signed': ''' ''',
            'short': ''' ''',
            'long': ''' ''',
            'type-modififer': ''' ''',
            'typedef': ''' ''',
            'constant': ''' ''',
            'macro': ''' ''',
            'wchar-t': ''' ''',
            'boolean':''' ''',
            'data-type': ''' ''',
            '2d-array': ''' ''',
            'array': ''' ''',
            'structure': ''' ''',
            'class': ''' ''',
            'union': ''' ''',
            'pointer': ''' ''',
            'enumeration': ''' ''',
            'integer': ''' ''',
            'floating-point': ''' ''',
            'double': ''' ''',
            'character': ''' ''',
            'string': ''' ''',
            'local-variable': ''' ''',
            'auto': ''' ''',
            'external': ''' ''',
            'static': ''' ''',
            'vector': ''' ''',
            'reference-variable': ''' ''',
            # Câu trả lời về các toán tử
            'decrement-operator': ''' ''',
            'increment-operator': ''' ''',
            'dereference-operator': ''' ''',
            'address_of-operator': ''' ''',
            'comma-operator': ''' ''',
            'ternary-operator': ''' ''',
            'binary-operator': ''' ''',
            'unary-operator': ''' ''',
            'shift-operator': ''' ''',
            'bitwise-operator': ''' ''',
            'logical-operator': ''' ''',
            'comparison-operator': ''' ''',
            'arithmetic-operator': ''' ''',
            'assignment-operator': ''' ''',
            'operator': ''' ''',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': ''' ''',
            'loop': ''' ''',
            'control-flow': ''' ''',
            'selection-statement': ''' ''',
            'iteration-statement': ''' ''',
            'jump-statement': ''' ''',
            'for': ''' ''',
            'while': ''' ''',
            'do-while': ''' ''',
            'switch': ''' ''',
            'break': ''' ''',
            'continue': ''' ''',
            'goto': ''' ''',
            'if-else': ''' ''',
            'if-else-if-ladder': ''' ''',
            'nested-if': ''' ''',
            # Câu trả lời về function
            'function': ''' ''',
            'parameter': ''' ''',
            'argument': ''' ''',
            'recursion': ''' ''',
            'pass-by-value': ''' ''',
            'pass-by-reference': ''' ''',
            'return': ''' ''',
            'return-type': ''' ''',
            'const-reference': ''' ''',
            'inline-function': ''' ''',
            'default-value': ''' ''',
            'main-function': ''' ''',
            'built-in-function': ''' ''',
            'lambda': ''' ''',
            'flowchart':''' ''',
            'introduction-to-programming':''' ''',
            'cout':''' ''',
            'cin':''' '''
        }

        all_answers_where = {
            'comment': ''' ''',
            'cplusplus': ''' ''',
            'include': ''' ''',
            'library': ''' ''',
            'namespace': ''' ''',
            'pseudo-code': ''' ''',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': ''' ''',
            'unsigned': ''' ''',
            'signed': ''' ''',
            'short': ''' ''',
            'long': ''' ''',
            'type-modififer': ''' ''',
            'typedef': ''' ''',
            'constant': ''' ''',
            'macro': ''' ''',
            'wchar-t': ''' ''',
            'boolean':''' ''',
            'data-type': ''' ''',
            '2d-array': ''' ''',
            'array': ''' ''',
            'structure': ''' ''',
            'class': ''' ''',
            'union': ''' ''',
            'pointer': ''' ''',
            'enumeration': ''' ''',
            'integer': ''' ''',
            'floating-point': ''' ''',
            'double': ''' ''',
            'character': ''' ''',
            'string': ''' ''',
            'local-variable': ''' ''',
            'auto': ''' ''',
            'external': ''' ''',
            'static': ''' ''',
            'vector': ''' ''',
            'reference-variable': ''' ''',
            # Câu trả lời về các toán tử
            'decrement-operator': ''' ''',
            'increment-operator': ''' ''',
            'dereference-operator': ''' ''',
            'address_of-operator': ''' ''',
            'comma-operator': ''' ''',
            'ternary-operator': ''' ''',
            'binary-operator': ''' ''',
            'unary-operator': ''' ''',
            'shift-operator': ''' ''',
            'bitwise-operator': ''' ''',
            'logical-operator': ''' ''',
            'comparison-operator': ''' ''',
            'arithmetic-operator': ''' ''',
            'assignment-operator': ''' ''',
            'operator': ''' ''',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': ''' ''',
            'loop': ''' ''',
            'control-flow': ''' ''',
            'selection-statement': ''' ''',
            'iteration-statement': ''' ''',
            'jump-statement': ''' ''',
            'for': ''' ''',
            'while': ''' ''',
            'do-while': ''' ''',
            'switch': ''' ''',
            'break': ''' ''',
            'continue': ''' ''',
            'goto': ''' ''',
            'if-else': ''' ''',
            'if-else-if-ladder': ''' ''',
            'nested-if': ''' ''',
            # Câu trả lời về function
            'function': ''' ''',
            'parameter': ''' ''',
            'argument': ''' ''',
            'recursion': ''' ''',
            'pass-by-value': ''' ''',
            'pass-by-reference': ''' ''',
            'return': ''' ''',
            'return-type': ''' ''',
            'const-reference': ''' ''',
            'inline-function': ''' ''',
            'default-value': ''' ''',
            'main-function': ''' ''',
            'built-in-function': ''' ''',
            'lambda': ''' ''',
            'flowchart':''' ''',
            'introduction-to-programming':''' ''',
            'cout':''' ''',
            'cin':''' '''
        }

        all_tutorials_link = {
            'comment': '''https://youtu.be/m-fT5o44Axw''',
            'cplusplus': '''https://youtu.be/m-fT5o44Axw''',
            'include': '''https://youtu.be/m-fT5o44Axw''',
            'library': '''https://youtu.be/m-fT5o44Axw''',
            'namespace': '''https://youtu.be/m-fT5o44Axw''',
            'pseudo-code': '''https://youtu.be/m-fT5o44Axw''',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': '''https://youtu.be/aFHDVyWm-PA''',
            'unsigned': '''https://youtu.be/aFHDVyWm-PA''',
            'signed': '''https://youtu.be/aFHDVyWm-PA''',
            'short': '''https://youtu.be/aFHDVyWm-PA''',
            'long': '''https://youtu.be/aFHDVyWm-PA''',
            'type-modififer': '''https://youtu.be/IH6_SqzAmhI''',
            'typedef': '''https://youtu.be/aFHDVyWm-PA''',
            'constant': ''' ''',
            'macro': ''' ''',
            'wchar-t': '''https://youtu.be/IH6_SqzAmhI''',
            'boolean':'''https://youtu.be/aFHDVyWm-PA''',
            'data-type': '''https://youtu.be/aFHDVyWm-PA''',
            '2d-array': '''https://youtu.be/Z6R6lLpiTaQ''',
            'array': '''https://youtu.be/9jeul0S3Vuo''',
            'structure': '''https://youtu.be/a_79OaVVZ3s''',
            'class': '''https://youtu.be/a_79OaVVZ3s''',
            'union': '''https://youtu.be/a_79OaVVZ3s''',
            'pointer': '''https://youtu.be/brmOY1Ca2So''',
            'enumeration': '''https://youtu.be/a_79OaVVZ3s''',
            'integer': '''https://youtu.be/aFHDVyWm-PA''',
            'floating-point': '''https://youtu.be/aFHDVyWm-PA''',
            'double': '''https://youtu.be/aFHDVyWm-PA''',
            'character': '''https://youtu.be/aFHDVyWm-PA''',
            'string': '''https://youtu.be/9FOz2TTGNSA''',
            'local-variable': '''https://youtu.be/aFHDVyWm-PA''',
            'auto': ''' ''',
            'external': ''' ''',
            'static': ''' ''',
            'vector': ''' ''',
            'reference-variable': '''https://youtu.be/brmOY1Ca2So''',
            # Câu trả lời về các toán tử
            'decrement-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'increment-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'dereference-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'address_of-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'comma-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'ternary-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'binary-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'unary-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'shift-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'bitwise-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'logical-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'comparison-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'arithmetic-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'assignment-operator': '''https://youtu.be/IH6_SqzAmhI''',
            'operator': '''https://youtu.be/IH6_SqzAmhI''',
            'scope-resolution-operator':''' ''',
            # Câu trả lời về control flow
            'if': '''https://youtu.be/RlK5TCJRKCk''',
            'loop': '''https://youtu.be/gBmj0xCizn8''',
            'control-flow': '''https://youtu.be/RlK5TCJRKCk''',
            'selection-statement': '''https://youtu.be/RlK5TCJRKCk''',
            'iteration-statement': ''' ''',
            'jump-statement': ''' ''',
            'for': '''https://youtu.be/gBmj0xCizn8''',
            'while': '''https://youtu.be/gBmj0xCizn8''',
            'do-while': '''https://youtu.be/gBmj0xCizn8''',
            'switch': '''https://youtu.be/gBmj0xCizn8''',
            'break': '''https://youtu.be/gBmj0xCizn8''',
            'continue': '''https://youtu.be/gBmj0xCizn8''',
            'goto': ''' ''',
            'if-else': '''https://youtu.be/RlK5TCJRKCk''',
            'if-else-if-ladder': '''https://youtu.be/RlK5TCJRKCk''',
            'nested-if': '''https://youtu.be/RlK5TCJRKCk''',
            # Câu trả lời về function
            'function': '''https://youtu.be/TTaEvxGEGG0''',
            'parameter': '''https://youtu.be/TTaEvxGEGG0''',
            'argument': '''https://youtu.be/TTaEvxGEGG0''',
            'recursion': '''https://youtu.be/yaUb5a7aCpE''',
            'pass-by-value': '''https://youtu.be/gxkJ_swJveg''',
            'pass-by-reference': '''https://youtu.be/gxkJ_swJveg''',
            'return': '''https://youtu.be/TTaEvxGEGG0''',
            'return-type': '''https://youtu.be/TTaEvxGEGG0''',
            'const-reference': '''''',
            'inline-function': '''https://youtu.be/TTaEvxGEGG0''',
            'default-value': '''https://youtu.be/TTaEvxGEGG0''',
            'main-function': '''https://youtu.be/m-fT5o44Axw''',
            'built-in-function': '''https://youtu.be/IH6_SqzAmhI?t=1076''',
            'lambda': ''' ''',
            'flowchart':'''https://youtu.be/HwifdLUvn0I''',
            'introduction-to-programming':'''https://youtu.be/m-fT5o44Axw''',
            'cout':'''https://youtu.be/IH6_SqzAmhI''',
            'cin':'''https://youtu.be/IH6_SqzAmhI'''
        }

        cpp_content_answer = " "

        #sql_intent_type = {
        #   'cpplus_why_asking':1,
        #   'cpplus_what_asking':2,
        #   'cpplus_when_asking':3,
        #   'cpplus_how_asking':4,
        #   'cpplus_where_asking':5
        #   'cpplus_example_asking':6
        #}

        # if(type(cpp_content) == list):
        #    for entity in cpp_content:
        #         TYPE = sql_intent_type[curr_intent]
        #         OBJECT = str(entity)
        #         cpp_content_asnwer = DataGet(TYPE,OBJECT)
        #         dispatcher.utter_message(text=cpp_content_answer)
        # else:
        #     TYPE = sql_intent_type[curr_intent]
        #     OBJECT = str(cpp_content)
        #     cpp_content_asnwer = DataGet(TYPE,OBJECT)
        #     dispatcher.utter_message(text=cpp_content_answer)

        def pull_answer(x):
            try:
                if curr_intent == 'cpplus_what_asking':
                    cpp_content_answer = all_answers_what[x]
                elif curr_intent == 'cpplus_why_asking':
                    cpp_content_answer = all_answers_why[x]
                elif curr_intent == 'cpplus_when_asking':
                    cpp_content_answer = "Invalid at the moment"
                elif curr_intent == 'cpplus_how_asking':
                    cpp_content_answer = all_answers_how[x]
                elif curr_intent == 'cpplus_where_asking':
                    cpp_content_answer = "Invalid at the moment"
                elif curr_intent == 'cpplus_example_asking':
                    cpp_content_answer = all_answers_example[x]
                elif curr_intent == 'cpplus_specific_video_tutorial_asking':
                    cpp_content_answer = all_tutorials_link[x]
                else:
                    cpp_content_answer = "Xin lỗi hiện tại mình chưa thể trả lời câu hỏi của bạn được :'("
            except KeyError:
                cpp_content_answer = "Xin lỗi bạn, hiện tại câu trả lời cho câu hỏi của bạn chưa có trong cơ sở dữ liệu. Vui lòng hãy hỏi câu khác !"
            return cpp_content_answer

        # if not cpp_content:
        #     dispatcher.utter_message(text='Xin lỗi bạn, hiện tại câu trả lời cho câu hỏi của bạn chưa có trong cơ sở dữ liệu. Vui lòng bạn hãy hỏi câu khác !')

        if(type(cpp_content) == list):
            for entity in cpp_content:
                dispatcher.utter_message(text=pull_answer(entity))
        else:
            dispatcher.utter_message(text=pull_answer(cpp_content))

        # if cpp_content_answer == " ":
        #     dispatcher.utter_message(text='Xin lỗi bạn, hiện tại câu trả lời cho câu hỏi của bạn chưa có trong cơ sở dữ liệu. Vui lòng bạn hãy hỏi câu khác !')
        if cpp_content_answer is None:
            cpp_content_answer = 'Xin lỗi bạn, hiện tại câu trả lời cho câu hỏi của bạn chưa có trong cơ sở dữ liệu. Vui lòng hãy hỏi câu khác !'

        return [SlotSet("cpp_content_answer", cpp_content_answer if cpp_content_answer is not None else [])]

class ValidateFlowcharQuestNumForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_flowchart_quest_num_form"

    @staticmethod
    async def flowchart_quest_num_db() -> List[Text]:
        """Database of supported flowchart question number"""

        return ['1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10',
                '11',
                '12',
                '13',
                '14',
                '15',
                '16',
                '17',
                '18',
                '19',
                '20',
                '21',
                '22',
                '23',
                '24',
                '25',
                '26',
                '27',
                '28',
                '29',
                '30',
                '31',
                '32',
                '33',
                '34',
                '35',
                '36',
                '37',
                '38',
                '39',
                '40',
                '41',
                '42',
                '43',
                '44',
                '45',
                '46',
                '47',
                '48',
                '49',
                '50',
                '51',
                '52',
                '53',
                '54',
                '55',
                '56',
                '57',
                '58',
                '59',
                '60',
                '61',
                '62',
                '63',
                '64',
                '65',
                '66',
                '67',
                '68',
                '69',
                '70',
                '71',
                '72',
                '73',
                '74',
                '75',
                '76',
                '77',
                '78',
                '79',
                '80',
                '81',
                '82',
                '83',
                '84',
                '85',
                '86',
                '87',
                '88',
                '89',
                '90',
                '91',
                '92',
                '93',
                '94',
                '95',
                '96',
                '97',
                '98',
                '99',
                '100']

    def validate_flowchart_quest_num(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if slot_value.lower() in self.flowchart_quest_num_db():
            # validation succeeded, set the value of the "flowchart_quest_num" slot to value
            return {"flowchart_quest_num": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"flowchart_quest_num": None}

class ValidateCppContentForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_cpp_content_form"

    @staticmethod
    async def cpp_content_db() -> List[Text]:
        """Database of supported c++ content"""

        return ['library',
                'namespace',
                'cplusplus',
                'comment',
                'include',
                'unsigned',
                'singed',
                'short',
                'long',
                'type-modifier',
                'typedef',
                'constant',
                'macro',
                'wchar-t',
                'boolean',
                'data-type',
                'variable',
                'array',
                '2d-array',
                'structure',
                'class',
                'union',
                'pointer',
                'enumeration',
                'integer',
                'floating-point',
                'double',
                'character',
                'string',
                'local-variable',
                'global-variable',
                'auto',
                'external',
                'static',
                'vector',
                'deference-operator',
                'reference-operator',
                'comma-operator',
                'ternary-operator',
                'binary-operator',
                'unary-operator',
                'shift-operator',
                'bitwise-operator',
                'logical-operator',
                'comparison-operator',
                'arithmetic-operator',
                'assignment-operator',
                'operator',
                'scope-resolution-operator',
                'if',
                'loop',
                'control-flow',
                'control-statement',
                'selection-statement',
                'iteration-statement',
                'jump-statement',
                'for',
                'while',
                'do-while',
                'switch',
                'break',
                'continue',
                'goto',
                'if-else',
                'if-else-if-ladder',
                'nested-if',
                'function',
                'parameter',
                'argument',
                'recursion',
                'pass-by-value',
                'pass-by-reference',
                'return',
                'return-type',
                'const-reference',
                'inline-function',
                'default-value',
                'main-function',
                'built-in-function',
                'lambda',
                'flowchart',
                'cout',
                'cin']
                
    def validate_cpp_content(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if slot_value.lower() in self.cpp_content_db():
            # validation succeeded, set the value of the "cpplus_content" slot to value
            return {"cpplus_content": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"cpplus_content": None}


#Use database to store user's information
# class ActionFirstName(Action):
#     def name(self) -> Text: 
#         return "action_first_name"

#     async def run(self, dispatcher: CollectingDispatcher, 
#                         tracker: Tracker, 
#                         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#         dispatcher.utter_message(template="utter_ask_first_name") 
#         return [SlotSet("firstN",tracker.latest_message['text'])]

# class ActionLastName(Action):
#     def name(self) -> Text: 
#         return "action_last_name"

#     async def run(self, dispatcher: CollectingDispatcher, 
#                         tracker: Tracker, 
#                         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#         dispatcher.utter_message(template="utter_ask_last_name") 
#         return [SlotSet("lastN",tracker.latest_message['text'])]
