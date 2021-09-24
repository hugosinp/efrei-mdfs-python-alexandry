import React, { useState } from 'react'
import axios from 'axios'
import { Container, Form, Col, Row, Button, InputGroup } from 'react-bootstrap'

function AddScreen() {
    const url = 'http://localhost:8000/api/book/create/'
    const [data, setData] = useState({
        name:"",
        author:"",
        category:"",
        date:"",
        description:"",
        price:"",
        image:""
    })

    function handle(e){
        const newData={...data}
        newData[e.target.id] = e.target.value
        setData(newData)
        console.log(newData)
    }

    function submit(e){
        e.preventDefault()
        axios.post(url, {
            name: data.name,
            author: data.author,
            category: data.category,
            date: data.date,
            description: data.description,
            price: data.price,
        })
        .then(res=> {
            console.log(res.data)
        })

        alert("Book Created !")
    }

    return (
        <div>
            <Container className="p-3">
                <h1>CREATE BOOK</h1>
                <Form onSubmit={(e)=> submit(e)}>
                    <Row className="mb-3">
                        <Form.Group as={Col} md="4">
                            <Form.Label>Book name</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="name"
                                value={data.name}
                                type="text"
                                placeholder="Book name"
                            />
                        <Form.Label>Author</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="author"
                                value={data.author}
                                type="text"
                                placeholder="Author"
                            />
                        <Form.Label>Category</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="category"
                                value={data.category}
                                type="text"
                                placeholder="Category"
                            />
                        <Form.Label>Published Date</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="date"
                                value={data.date}
                                type="date"
                                placeholder="Published Date"
                            />
                        <Form.Label>Description</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="description"
                                value={data.description}
                                type="text"
                                placeholder="Description"
                            />
                        <Form.Label>Price</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="price"
                                value={data.price}
                                type="number"
                                placeholder="Price"
                            />
                        <Form.Label>Image</Form.Label>
                            <Form.Control
                                required
                                onChange={(e)=>handle(e)}
                                id="image"
                                value={data.image}
                                type="file"
                                placeholder="Image"
                            />
                        </Form.Group>
                        
                    </Row>
                    <Button type="submit">Submit form</Button>
                </Form>
            </Container>
        </div>
    )
}

export default AddScreen
