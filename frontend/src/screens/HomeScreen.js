import React, { useState, useEffect } from 'react'
import axios from 'axios'

import { Container, Row, Col } from 'react-bootstrap'

import Book from '../components/Book'

function HomeScreen() {
    const [books, setBooks] = useState([])

    useEffect(() => {

        async function fetchBooks(){
            const { data } = await axios.get('http://localhost:8000/api/books/')
            setBooks(data)
        }
        
        fetchBooks()

    }, [])


    return (
        <div className="py-3">
            <Container>
                <h1>Books</h1>
                <Row>
                    {books.map(book => (
                        <Col key={book._id} sm={12} md={6} lg={4} xl={3}>
                            <Book book={book} />
                        </Col>
                    ))}                    
                </Row>
            </Container>
        </div>
    )
}

export default HomeScreen
