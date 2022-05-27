'use strict';

const e = React.createElement;

//function Flipcard(props){
//    return(
//        <div class="flip-card">
//          <div class="flip-card-inner">
//            <div class="flip-card-front">
//              <img src="static/images/introduction.jpg" alt="Avatar" style="width:300px;height:300px;">
//            </div>
//            <div class="flip-card-back">
//              <p>{props.text}</p>
//            </div>
//          </div>
//        </div>
//    )
//}

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
    );
  }
}
// Render Root Functions
const domContainer = document.querySelector('#skillPage');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));
