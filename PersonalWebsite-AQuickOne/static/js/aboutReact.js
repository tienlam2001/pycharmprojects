'use strict';

const e = React.createElement;

function Flipcard(props){
    return(
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <img src="static/images/introduction.jpg" alt="Avatar" style="width:300px;height:300px;"></img>
            </div>
            <div class="flip-card-back">
              <p>{props.text}</p>
            </div>
          </div>
        </div>
    )
}

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
	   <div id ="aboutReact">
			 <h1 id ="aboutTitle"> About me </h1>
			 <div id ="sectionId">
			    <section class = "about aboutCommon">
                    <Flipcard text ="Hello, My name is Lam, I am 20 years old. I am currently a college student, pursing dual degree Computer Science and Finance. I am usually coding, read, and workout in my freetime. Staying busy is my life goal, just because it got boring by siting around."/>

			    </section>
			    <section class = "hobbies aboutCommon">
			        <ul>
			            <li> Coding </li>
			            <li> Investment</li>
			            <li> Read books or annual reports</li>
			            <li> Study new skills</li>
			        </ul>
			    </section>
			 </div>
		 </div>
    );
  }
}
// Render Root Functions
const domContainer = document.querySelector('#aboutPage');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));
