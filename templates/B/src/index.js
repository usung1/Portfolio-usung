import React from 'react';
// import ReactDOM from 'react-dom/client';
import './index.css';

import ReactDOM from "react-dom";

const Apps = () => {
  return (

    <>
    <div id="login">
        <form method="POST">
            <h1>Pystagram</h1>
            {/* {% csrf_token %}
            {{ form.as_p}} */}
            <button type="submit" class="btn btn-login">로그인</button>
            <a href="/users/signup/">회원가입 페이지로 이동</a>

        </form>
    </div>
    </>
  );
}
ReactDOM.render(<Apps />, document.getElementById("root"));

