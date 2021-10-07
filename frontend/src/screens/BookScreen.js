import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { Row, Col, ListGroup, Container } from 'react-bootstrap'


function BookScreen({ match }) {
    const [book, setBook] = useState([])

    useEffect(() => {

        async function fetchBook(){
            const { data } = await axios.get(`http://localhost:8000/api/books/${match.params.id}`)
            setBook(data)
        }

        fetchBook()

    }, [])

    async function deleteBook(){
        const { data } = await axios.delete(`http://localhost:8000/api/book/delete/${match.params.id}`)
        deleteBook(data)
        window.location.reload()
        alert("Book deleted")
    }

    return (
        <div>
            <Container className="">
                <Link to='/' className='btn btn-light my-3'>Go Back</Link>

                <Row>
                    <Col md={5}>
                        <img src={book.image} style={{height:"450px"}} alt={book.name} />
                    </Col>

                    <Col md={4}>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                <h3>{book.name}</h3>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                Description : {book.description}
                            </ListGroup.Item>
                        </ListGroup>
                    </Col>

                    <Col md={3}>
                        <ListGroup variant='flush'>

                            <ListGroup.Item>
                                <Row>
                                    <Col>Price :</Col>
                                    <Col>
                                        <strong>${book.price}</strong>
                                    </Col>
                                </Row>
                            </ListGroup.Item>

                            <ListGroup.Item>
                                <div className="d-grid gap-2">
                                    <Link to={`/book/update/${match.params.id}`} className='btn btn-danger my-3'>Edit book</Link>
                                </div>
                                <Link to='/' onClick={deleteBook} className='btn btn-danger my-3'>Delete</Link>

                            </ListGroup.Item>

                        </ListGroup>
                    </Col>
                    
                </Row>
             </Container>
        </div>
    )
                


    
}

export default BookScreen
