"""Seed database with initial data"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session, engine
from app.models import Base, Category, Subcategory, Tag

async def create_seed_data():
    """Create initial categories, subcategories, and tags"""
    
    # Create all tables first
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with async_session() as session:
        # Check if data already exists
        existing_categories = await session.execute(
            "SELECT COUNT(*) FROM categories"
        )
        if (await existing_categories.fetchone())[0] > 0:
            print("Seed data already exists, skipping...")
            return
        
        # Categories
        categories_data = [
            {"name": "Work", "color": "#3B82F6", "description": "Professional tasks and projects"},
            {"name": "Personal", "color": "#10B981", "description": "Personal activities and goals"},
            {"name": "Learning", "color": "#F59E0B", "description": "Education and skill development"},
            {"name": "Health", "color": "#EF4444", "description": "Exercise, health, and wellness"},
            {"name": "Social", "color": "#8B5CF6", "description": "Social activities and relationships"},
            {"name": "Maintenance", "color": "#6B7280", "description": "Household and maintenance tasks"},
        ]
        
        categories = []
        for cat_data in categories_data:
            category = Category(**cat_data)
            session.add(category)
            categories.append(category)
        
        await session.flush()  # Get IDs
        
        # Subcategories
        subcategories_data = [
            # Work subcategories
            {"name": "Development", "category_id": categories[0].id},
            {"name": "Meetings", "category_id": categories[0].id},
            {"name": "Planning", "category_id": categories[0].id},
            {"name": "Documentation", "category_id": categories[0].id},
            
            # Personal subcategories
            {"name": "Hobbies", "category_id": categories[1].id},
            {"name": "Family Time", "category_id": categories[1].id},
            {"name": "Errands", "category_id": categories[1].id},
            
            # Learning subcategories
            {"name": "Online Courses", "category_id": categories[2].id},
            {"name": "Reading", "category_id": categories[2].id},
            {"name": "Practice", "category_id": categories[2].id},
            
            # Health subcategories
            {"name": "Exercise", "category_id": categories[3].id},
            {"name": "Meal Prep", "category_id": categories[3].id},
            {"name": "Medical", "category_id": categories[3].id},
        ]
        
        for subcat_data in subcategories_data:
            subcategory = Subcategory(**subcat_data)
            session.add(subcategory)
        
        # Tags
        tags_data = [
            {"name": "Urgent", "color": "#DC2626", "description": "High priority tasks"},
            {"name": "Important", "color": "#EA580C", "description": "Important but not urgent"},
            {"name": "Quick", "color": "#059669", "description": "Tasks that take < 30 minutes"},
            {"name": "Deep Work", "color": "#7C3AED", "description": "Tasks requiring focus"},
            {"name": "Creative", "color": "#DB2777", "description": "Creative and brainstorming tasks"},
            {"name": "Review", "color": "#0284C7", "description": "Review and feedback tasks"},
            {"name": "Research", "color": "#0891B2", "description": "Research and analysis"},
            {"name": "Administrative", "color": "#64748B", "description": "Admin and paperwork"},
        ]
        
        for tag_data in tags_data:
            tag = Tag(**tag_data)
            session.add(tag)
        
        await session.commit()
        print(f"Created {len(categories_data)} categories, {len(subcategories_data)} subcategories, and {len(tags_data)} tags")

if __name__ == "__main__":
    asyncio.run(create_seed_data())