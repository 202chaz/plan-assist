import { Modal, Col, Spinner, Image, Row } from "react-bootstrap"

export default function AlertModal({ show, handleClose, getType }) {

  const quotes = [
    "Can trees log in if they want to surf the internet?",
    "Can computers eat microchips for snacks?",
    "If your mentor tells you ‘you can be anyone you want to be’ why is identity theft a crime?",
    "A few math jokes are funny, can you name sum?",
    "Do you want it done fast or right",
    "Before you marry a person, you should first make them use a computer with slow Internet to see who they really are.",
    "I love being married. It's so great to find that one special person you want to annoy for the rest of your life.",
    "Truth hurts. Maybe not as much as jumping on a bicycle with a seat missing, but it hurts.",
    "Common sense is like deodorant. The people who need it most never use it.",
    "The difference between screwing around and science is writing it down.",
    "To steal ideas from one person is plagiarism; to steal from many is research.",
    "If we knew what it was we were doing, it would not be called research, would it?",
    "If you torture the data long enough, it will confess.",
    "I'm sure the universe is full of intelligent life. It's just been too intelligent to come here.",
    "Computers are useless. They can only give you answers.",
    "Basic research is what I am doing when I don't know what I am doing.",
    "I won’t be impressed with technology until I can download food.",
    "Wi-Fi went down for five minutes, so I had to talk to my family. They seem like nice people.",
    "Life was much easier when Apple and Blackberry were just fruits.",
    "The point is not how we use a tool, but how it uses us."
  ]

  const getQuote = () => {
    let index = Math.floor(Math.random() * quotes.length + 1);
    return quotes[index]
  }

  return(
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header>
          <Modal.Title>Retreiving Data ...</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Col className="text-center">
            <Spinner animation="grow" role="status" variant={'info'}>
              <span className="sr-only" style={{marginLeft: 'auto', marginRight: 'auto'}}></span>
            </Spinner>
          </Col>
          { getType && getType === 'pdf' &&
            <Row className="align-items-center mt-4">
              <Col sm={2}>
                <Image src="chatgpt-logo.png" className="gpt-icon" />
              </Col>
              <Col sm={10}>
                <h5>Processing with GPT-3.5 Turbo</h5>
              </Col>
              <Col sm={12}>
                <figure className="text-center mt-4">
                  <figcaption className="blockquote-footer">
                    {getQuote()} <cite title="Source Title">Your Assistant</cite>
                  </figcaption>
                </figure>
              </Col>
            </Row>
          }
        </Modal.Body>
      </Modal>
    </>
  )
}