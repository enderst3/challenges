var TweetBox = React.createClass({
  getInitialState: function(){
    return {
      text: ""
    };
  },
  handleChange: function(event) {
    this.setState({ text: event.target.value });
//     console.log(event.target.value);
  },
  render: function(){
    return (
      <div className="well clearfix">
        <textarea className="form-control"
                  onChange={this.handleChange}></textarea>
        <br/>
        <button className="btn btn-primary pull-right"
                disabled={this.state.text.length === 0}>Tweet</button>
      </div>
    );
  }
});


ReactDOM.render(
  <TweetBox />,
  document.getElementById("container")
);
