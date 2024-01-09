import { Modal, Col, Spinner } from "react-bootstrap"

export default function AlertModal({ show, handleClose }) {
  return(
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header>
          <Modal.Title>Analyzing file</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Col className="text-center">
            <Spinner animation="border" role="status">
              <span className="sr-only" style={{marginLeft: 'auto', marginRight: 'auto'}}></span>
            </Spinner>
          </Col>
        </Modal.Body>
      </Modal>
    </>
  )
}