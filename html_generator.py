import datetime
def generate_html_report(email, results):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Holehe Results - {email}</title>
        <!-- Modern UI Libraries -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            :root {{ --bs-body-bg: #f8f9fa; }}
            body {{ padding-top: 2rem; }}
            .card {{ 
                transition: transform 0.2s;
                border: none;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .card:hover {{ 
                transform: translateY(-5px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            .account-found {{ color: #198754; }}
            .account-not-found {{ color: #dc3545; }}
            .header-card {{
                background: linear-gradient(135deg, #4158D0 0%, #C850C0 46%, #FFCC70 100%);
                color: white;
            }}
            .category-header {{
                border-left: 4px solid #4158D0;
                padding-left: 1rem;
                margin: 2rem 0;
            }}
            .stats-card {{
                background: white;
                border-radius: 15px;
                padding: 1rem;
                margin-bottom: 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="card header-card mb-4">
                <div class="card-body">
                    <div class="d-flex align-items-center">
                        <i class="material-icons fs-1 me-3">search</i>
                        <div>
                            <h1 class="mb-0">Holehe Results</h1>
                            <p class="mb-0">Email checked: {email}</p>
                            <small>Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Stats Overview -->
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="stats-card">
                        <h5><i class="fas fa-check-circle text-success"></i> Found Accounts</h5>
                        <h2>{len([r for r in results if r.get('exists')])}</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stats-card">
                        <h5><i class="fas fa-search"></i> Total Checked</h5>
                        <h2>{len(results)}</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stats-card">
                        <h5><i class="fas fa-clock text-warning"></i> Rate Limited</h5>
                        <h2>{len([r for r in results if r.get('rateLimit')])}</h2>
                    </div>
                </div>
            </div>

            <!-- Results Grid -->
            <div class="category-header">
                <h3><i class="material-icons align-middle">list_alt</i> Detailed Results</h3>
            </div>
            <div class="row">
    """
    
    # Group results by category
    categories = {}
    for result in results:
        category = result.get('category', 'Other')
        if category not in categories:
            categories[category] = []
        categories[category].append(result)
    
    # Generate cards for each category
    for category, items in categories.items():
        html += f"""
            <div class="col-12">
                <h4 class="mt-4 mb-3">
                    <i class="fas fa-folder-open"></i> {category.replace('_', ' ').title()}
                </h4>
            </div>
        """
        
        for result in items:
            exists = result.get('exists', False)
            status_class = 'account-found' if exists else 'account-not-found'
            icon = 'check_circle' if exists else 'cancel'
            
            html += f"""
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title {status_class}">
                                <i class="material-icons align-middle">{icon}</i> {result['name']}
                            </h5>
                            <p class="card-text">
                                <span class="badge bg-{'success' if exists else 'danger'}">
                                    {'Account Found' if exists else 'No Account'}
                                </span>
                            </p>
                            <small class="text-muted">
                                <i class="fas fa-info-circle"></i> Method: {result.get('method', 'Unknown')}
                            </small>
                        </div>
                    </div>
                </div>
            """
    
    html += """
            </div>
        </div>
        <!-- Scripts -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    filename = f"holehe_report_{email}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    
    return filename
