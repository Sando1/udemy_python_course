import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow{
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "My Window"

    Item{
        id: page
        visible: true
        width: parent.width

        Rectangle {
            id: rect1
            height:160
            color: "#ff0000"
            width: parent.width

            Text{
                id: mainText
                text: "I am text"
                height: 50
                width: parent.width
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                color: "#aaa"
            }

            Button{
                id: mainButton
                text: "Push Me"
                anchors.top:mainText.bottom
                onClicked:{
                    if(rect1.color == "#000"){
                        rect1.color = "#f00"
                    } else {
                        rect1.color = "#000"
                    }
                }
            }
        }
    }
}
