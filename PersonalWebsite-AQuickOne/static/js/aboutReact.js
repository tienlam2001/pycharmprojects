'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
	   <div id ="certificationContainer">
			 <div>
			    <h1>Hello World</h1>
			 </div>
		 </div>
    );
  }
}
// Render Root Functions
const domContainer = document.querySelector('#aboutPage');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));
