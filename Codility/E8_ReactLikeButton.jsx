import cx from 'classnames';
import { Component } from 'react';

export default class LikeButton extends Component {
    
    constructor(props){
        super(props);
        this.state = {
            likes: 100,
            isLiked: false
        };
    }    

    handleClick = () => {
        this.setState((prevState) => ({
            likes: !prevState.isLiked ? prevState.likes + 1 : prevState.likes - 1,
            isLiked: !prevState.isLiked
        }));
        console.log('clicked')
    };

    render() {
        return (
            <>
                <div>
                    <h2>Like Button</h2>
                </div>
                <button onClick={this.handleClick} className={`like-button ${this.state.isLiked ? 'liked' : ''}`}>
                    Like | <span className="likes-counter">{this.state.likes}</span>
                </button>
                <style>{`
                    .like-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                    .liked {
                        font-weight: bold;
                        color: #1565c0;
                    }
                    .likes-counter{
                        
                    }
                `}</style>
            </>
        );
    }
}