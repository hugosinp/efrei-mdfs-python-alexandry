import React from 'react'
import { Container, Navbar, Nav, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

function Header() {
    return (
        <div>
            <header>
                <Navbar bg="light" expand="lg">
                    <Container>
                        <LinkContainer to='/'>
                            <Navbar.Brand>Library Admin Panel</Navbar.Brand>
                        </LinkContainer>
                        
                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                        <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                            <LinkContainer to='/'>
                                <Nav.Link href="">Home</Nav.Link>
                            </LinkContainer>
                        </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
            </header>    
        </div>
    )
}

export default Header
