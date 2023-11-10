import React from "react";
import './InputBox.css'
import { useRecoilValue } from "recoil";
import { imageState } from "../../store";

function InputBox(props) {
  // TODO : 이미지 입력 만들기
  const imgFile = useRecoilValue(imageState);
  
  return (
        <div className="InputBox">
          {
            imgFile.isEmpty ?
            <p>이미지를 업로드 해주세요.</p> :
            <img src={imgFile.img} />
          }
        </div>
    )
};
export default InputBox;