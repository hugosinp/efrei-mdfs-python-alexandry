import React from 'react'
import { Card, Col } from 'react-bootstrap'
import { Link } from 'react-router-dom'


function Book({ book }) {

    return (
        <Card className="my-2 p-3 rounded">
            <Link to={`/books/${book._id}`}>
                <Col md={5}>
                    <Card.Img src={book.image} style={{width:"240px", height:"300px"}} />
                </Col>
            </Link>

            <Card.Body>
                <Link to={`/books/${book._id}`}>
                    <Card.Title as="div">
                        <strong>{book.name}</strong>
                        <p>{book.author}</p>
                    </Card.Title>
                </Link>    

                <Card.Text as="h5">
                    Qty : {book.countInStock}
                </Card.Text>

            </Card.Body>

        </Card>
    )
}

export default Book
