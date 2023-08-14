
// AWS SDK import
// AWS 설정
AWS.config.update({
    region: '',
    credentials: new AWS.Credentials('', '')
});

var global_data = "";
var global_id = "";



// 사용자 입력을 Lex 봇으로 전송하는 함수
function sendUserInput(inputText) {
    // AWS Lex V2 클라이언트 생성
    const lexClient = new AWS.LexRuntimeV2();

    const params = {
        botId: '',
        botAliasId: '',
        localeId: '', // 봇의 언어 설정에 따라 다름
        sessionId: '',
        text: inputText
    };
    return lexClient.recognizeText(params).promise();
}
// 웹 페이지에서 사용자 입력을 받고, Lex 봇과 상호 작용하는 함수
function sendMessage() {
    const userInput = document.getElementById('userInput').value.trim();
    handleChat(userInput);

}

function handleChat(userInput) {
    if (userInput !== '') {
        appendMessage(sender_name, userInput);
        document.getElementById('userInput').value = '';

        if (userInput == "상품 링크" || userInput == "다른 상품") {
            iteminformation(userInput);
        }
        else {
            sendLex(userInput);
        }
    }
}

function iteminformation(message) {
    if (message == "상품 링크") {
        // console.log(global_data);
        appendMessage('챗봇', global_data);
    }
    else if (message == "다른 상품") {
        sendToServer_item(global_id)
            .then(data => {
                // 서버로부터 받은 응답 처리
                message_kind(data);
            });
    }
}



function sendLex(userInput) {
    // 사용자 입력을 Lex 봇에 보내기
    sendUserInput(userInput)
        .then(response => {
            // Lex의 응답 처리
            const botMessage = response.messages[0].content;

            if (botMessage == "999") {
                sendToServer_mall()
                    .then(data => {
                        // 서버로부터 받은 응답 처리
                        message_kind(data);
                    });
            }
            else {
                sendToServer(botMessage)
                    .then(data => {
                        // 서버로부터 받은 응답 처리
                        message_kind(data);
                    });
            }

        })
        .catch(err => {
            console.error('Error:', err);
        });
}

function message_kind(data) {

    // 서버로 받은 내용에 | 이 있는 경우 (상품 링크 존재 여부 확인)
    var dataArray = "";

    if (data.response.information) {
        const information = data.response.information;
        const delimiter = "|";
        dataArray = information.includes(delimiter) ? information.split(delimiter) : [information];
        global_id = data.response.id;
    }


    if (dataArray.length == 2) {
        global_data = dataArray[1];
        // console.log(dataArray[0]);
        appendMessage('챗봇', dataArray[0]);
    }
    else {
        if (!dataArray) {
            if (data.response.id) {
                dataArray = "더 이상 상품 정보가 없습니다. \n다른 매장 상품을 이용해주세요";
                // console.log(dataArray);
                appendMessage('챗봇', dataArray);
                sendToServer_mall()
                    .then(data => {
                        // console.log("확인용 " + data);
                        // 서버로부터 받은 응답 처리
                        message_kind(data);
                    });
            }
        }
        else {
            // console.log(dataArray);
            appendMessage('챗봇', dataArray);
        }

    }
    if (data.response.item) {
        // console.log(data.response.item);
        appendItem(data);
    }
    else if (data.response.image) {
        // console.log(data.response.image);
        appendImage(data);
    }
    if (data.response.button) {
        // console.log(data.response.button);
        appendButton(data);
    }
    
}

// 챗봇의 응답을 Flask 서버로 보내는 함수    db 연동을 통해 넘버링과 일치한 db 값의 찾기
function sendToServer(botMessage) {
    // console.log(botMessage);

    return fetch('/api/find_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ botMessage: botMessage })
    })
        .then(response => response.json());
}

// 챗봇의 응답을 Flask 서버로 보내는 함수    업체의 아이템 찾기
function sendToServer_item(botMessage) {
    // console.log(botMessage);

    return fetch('/api/other_item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: botMessage })
    })
        .then(response => response.json());
}

// 챗봇의 응답을 Flask 서버로 보내는 함수  업체의 쇼핑몰 찾기
function sendToServer_mall() {
    return fetch('/api/search_mall', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: ""
    })
        .then(response => response.json());
}


// 대화 기록 표시 함수
function appendMessage(sender, message) {
    var chatlog = document.getElementById('chatlog');
    var messageElement = document.createElement('div');
    messageElement.className = sender === sender_name ? 'user-message card float-right' : 'bot-message card';

    // sender를 card 밖에서 생성하여 표시
    var senderElement = document.createElement('div');

    senderElement.className = sender === sender_name ? 'user-sender-text send float-right' : 'bot-sender-text send';
    var sendElement = document.createElement('div');
    sendElement.className = 'sender-body';
    var sendTextElement = document.createElement('p');
    sendTextElement.className = 'sender-text';
    sendTextElement.innerText = sender === '챗봇' ? "천안 청년몰" : sender;

    sendElement.appendChild(sendTextElement);
    senderElement.appendChild(sendElement);

    // Bootstrap card 요소 생성
    var cardElement = document.createElement('div');
    cardElement.className = 'card-body';

    // 실제 메시지를 card 내에 텍스트로 표시
    var messageTextElement = document.createElement('p');
    messageTextElement.className = 'card-text';
    messageTextElement.innerText = message;
    cardElement.appendChild(messageTextElement);

    // card를 메시지 요소에 삽입
    messageElement.appendChild(cardElement); // card를 그 다음에 삽입

    chatlog.appendChild(senderElement);
    chatlog.appendChild(messageElement);

    
    // 새 메시지가 추가되었을 때 스크롤 아래로 이동
    const chatscroll = document.getElementById('chatMessages');
    chatscroll.scrollTop = chatscroll.scrollHeight;
}


function appendButton(data) {
    const buttonDiv = document.createElement('div');
    buttonDiv.className = 'button';

    const buttonTexts = data.response.button.split(' | ');
    buttonTexts.forEach(buttonText => {
        const buttonElement = document.createElement('button');
        buttonElement.innerText = buttonText;
        // 버튼 클릭 이벤트 처리 추가
        buttonElement.addEventListener('click', function () {
            //     // 버튼 클릭 처리 로직
            handleChat(buttonText);
        });
        buttonDiv.appendChild(buttonElement);
    });

    document.getElementById('chatlog').appendChild(buttonDiv);
    
    // 새 메시지가 추가되었을 때 스크롤 아래로 이동
    const chatscroll = document.getElementById('chatMessages');
    chatscroll.scrollTop = chatscroll.scrollHeight;
}

function appendImage(data) {
    const imageElement = document.createElement('img');
    imageElement.src = data.response.url;
    imageElement.className = 'image';

    document.getElementById('chatlog').appendChild(imageElement);
    
    // 새 메시지가 추가되었을 때 스크롤 아래로 이동
    const chatscroll = document.getElementById('chatMessages');
    chatscroll.scrollTop = chatscroll.scrollHeight;
}

function appendItem(data) {
    if (data.response.item.image) {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';

        const itemName = document.createElement('p');
        itemName.innerText = data.response.item.name;

        const itemImage = document.createElement('img');
        itemImage.src = data.response.item.url;
        itemImage.className = 'item-image';

        itemDiv.appendChild(itemImage);

        document.getElementById('chatlog').appendChild(itemDiv);
        
        // 새 메시지가 추가되었을 때 스크롤 아래로 이동
        const chatscroll = document.getElementById('chatMessages');
        chatscroll.scrollTop = chatscroll.scrollHeight;
    }
}