<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechSky</title>
</head>
<body>
    <div class="container">
        <h1>Python Flask CRUD Application</h1>
        <div>
            <h2>Student List <button>Add Student</button></h2>
            <div id="myModal">
                <div>
                    <div>
                        <h5>Please Add New Student</h5>
                        <button>&times;</button>
                    </div>
                    <div>
                        <form action="{{ url_for('insert') }}" method="POST">
                            <div>
                                <label>Full Name</label>
                                <input type="text" name="name" placeholder="Enter Full Name">
                            </div>
                            <div>
                                <label>Email</label>
                                <input type="text" name="email" placeholder="Enter Email">
                            </div>
                            <div>
                                <label>Phone Number</label>
                                <input name="phone" type="text" placeholder="Enter Phone Number">
                            </div>
                            <button type="submit">Save</button>
                        </form>
                    </div>
                </div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>S/N</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in students %}
                    <tr>
                        <td>{{row.0}}</td>
                        <td>{{row.1}}</td>
                        <td>{{row.2}}</td>
                        <td>{{row.3}}</td>
                        <td>
                            <a href="/update/{{row.0}}" data-toggle="modal" data-target="#modaledit{{row.0}}">Edit</a>
                            <a href="/delete/{{row.0}}" onclick="return confirm('Are you sure you want to delete?')">Delete</a>
                        </td>
                    </tr>
                    <div id="modaledit{{row.0}}">
                        <div>
                            <div>
                                <h5>Update Student Details</h5>
                                <button>&times;</button>
                            </div>
                            <div>
                                <form action="{{ url_for('update') }}" method="POST">
                                    <input type="hidden" name="id" value="{{row.0}}">
                                    <div>
                                        <label>Full Name</label>
                                        <input value="{{row.1}}" type="text" name="name" placeholder="Enter Full Name">
                                    </div>
                                    <div>
                                        <label>Email</label>
                                        <input value="{{row.2}}" type="text" name="email" placeholder="Enter Email">
                                    </div>
                                    <div>
                                        <label>Phone Number</label>
                                        <input value="{{row.3}}" name="phone" type="text" placeholder="Enter Phone Number">
                                    </div>
                                    <button type="submit">Update</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
