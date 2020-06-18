/**
 * CSRF対策用のcookieを取得する
 * 
 * @param {string} name csrftoken文字列
 * @returns {string} cookieValue クッキー文字列
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * CSRF対象外の送信タイプか判定する
 * 
 * @param {string} method 送信タイプ 
 * @returns {boolean}} CSRF対象外の送信タイプならtrue
 */
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * ajax通信のセットアップ
 */
function ajaxSetup() {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}

/**
 * 画像データアップロード
 * 
 * @param {string} url ajax呼び出しパス 
 */
function uploadImageFile(url) {
    // canvasを画像データに変換
    $(".picture").each(function (i, canvas) {
        canvas.toBlob(function (blob) {
            var formData = new FormData();
            var name = "face_image";
            var fileName = "image_" + i + ".jpg";
            formData.append(name, blob, fileName);

            // <input type="file"> の内容はJavaScriptでアクセスできない
            // よってajaxで画像をアップロードする
            $.ajax({
                method: "POST",
                url: url,
                data: formData, // 配列にまとめると取得できない
                async: false, // 同期通信とする。非推奨だが重い処理ではないためOKとする
                processData: false,  // jQuery がデータを処理しないよう指定
                contentType: false,  // jQuery が contentType を設定しないよう指定

            }).then(
                function (data) {// 通信成功時
                    console.log("画像アップロードに成功しました。" + data.file_name);
                },
                function (jqXHR, textStatus, errorThrown) { // 通信失敗時
                    console.log("画像アップロードに失敗しました。");
                    console.log("jqXHR       : " + jqXHR.status); // HTTPステータスが取得
                    console.log("textStatus  : " + textStatus);    // タイムアウト、パースエラー
                    console.log("errorThrown : " + errorThrown.message); // 例外情報
                }

            ).always(function () {
                console.log('ajaxの通信処理が完了しました。');
            });
        }, "image/jpg", 0.95);
    })
}

/**
 * カメラ撮影のセットアップ
 */
function cameraSetup() {
    // カメラ設定に使用する定数を定義
    const video = $("#camera").get(0);
    const $canvases = $(".picture");
    const se = $("#se").get(0);

    // カメラ設定
    const constraints = {
        audio: false,
        video: {
            width: 150,
            height: 150,
            facingMode: "user"
        }
    };

    // カメラを<video>と同期
    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
            };
        })
        .catch((err) => {
            console.log(err.name + ": " + err.message);
        });

    settings = { video: video, canvases: $canvases, se: se };
    return settings
}

/**
 * 写真撮影を行う
 * 
 * @param {array} settings 設定ファイル 
 */
function takePhoto(settings) {
    const len = settings.canvases.length; // 総撮影枚数
    var i = 0; // 現在の撮影数

    // 1秒ごとにカメラ撮影を実行する
    var timer = setInterval(() => {
        // clearIntervalで即座に停止するわけではないため
        // 総撮影枚数 - 1の段階でclearIntervalを実行する
        if (i >= len - 1) {
            clearInterval(timer);
        };

        var canvas = settings.canvases.get(i);
        const ctx = canvas.getContext("2d");

        // 演出的な目的で一度映像を止めてSEを再生、0.5秒後にカメラを再開する
        settings.video.pause();
        settings.se.play();
        setTimeout(() => {
            settings.video.play();
        }, 500);

        // canvasに画像を貼り付ける
        ctx.drawImage(settings.video, 0, 0, canvas.width, canvas.height);
        i++;
    }, 1000);
}